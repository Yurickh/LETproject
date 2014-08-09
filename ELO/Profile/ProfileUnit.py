#coding: utf-8

## @file ProfileUnit.py
#   Este arquivo é responsável pelo armazenamento de todas as camadas 
# correspondentes ao módulo de perfil. 
#   Os métodos aqui são criados e chamados pela Factory (MainUnit.py)
# quando necessários. Eles são responsáveis pelo redirecionamento do usuário
# para páginas diferentes dependendo do tipo de usuário, edição de dados 
# pessoais, visualização de informações relativas aos cursos.

from abc import*
import json

import ELO.locale.index as lang

from ELO.models import Student, Professor
from Profile.forms import (
    NameForm, 
    LanguageForm,
    SexForm,
    BiosForm,
    InterestsForm,
    AvatarForm)

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import translation
from django import forms

## Interface para a camada de Apresentação de Usuário do módulo Profile.
#   É responsável pelo carregamento do template correto e processa os 
#   dados inseridos nos formulários de Perfil.
class IfUiProfile:
    __metaclass__ = ABCMeta

    ## Força a criação da camada subjacente.
    def __init__(self, bus):
        try:
            self.bus = bus
        except TypeError as exc:
            del self
            raise exc

    @property
    def bus(self):
        return self.__bus

    @bus.setter
    def bus(self, value):
        if isinstance(value, IfBusProfile):
            self.__bus = value
        else:
            raise TypeError("Expected IfBusProfile instance at \
                UiProfile.__bus. Received " + 
                str(type(value)) + " instead.")

    @bus.deleter
    def bus(self):
        del self.__bus

    ## 'Run' é o principal método de qualquer classe de apresentação. 
    #   Este método permite a Factory dar o controle do programa 
    #   módulo.
    @abstractmethod
    def run(self, request): pass


## Interface para a camada de Negócio do módulo de perfil.
#   É responsável por executar a atualização do Cookie de dados do
#   usuário, bem como a devida recuperação de dados para o sistema.
class IfBusProfile:
    __metaclass__ = ABCMeta

    ## Força a criação das camadas subjacentes.
    def __init__(self, pers):
        try:
            self.pers = pers
        except TypeError as exc:
            del self
            raise exc

    @property
    def pers(self):
        return self.__pers
    
    @pers.setter
    def pers(self, value):
        if isinstance(value, IfPersProfile):
            self.__pers = value
        else:
            raise TypeError("Expected IfPersProfile instance at \
                BusProfile.__pers. Received " + 
                str(type(value)) + "instead.")

    @pers.deleter
    def pers(self):
        del self.__pers

    ## Atualiza os dados de usuário no cookie de sessão.
    @abstractmethod
    def refreshUser(self, request): pass

    ## Edita um dos dados de usuário no cookie E no banco de dados.
    #   Retorna o valor editado.
    #
    #   @arg field      Nome do campo que deve ser editado.
    #
    #   @arg form       Objeto form que contém os dados.
    @abstractmethod
    def editField(self, request, field, form): pass


## Interface para a camada de Persistência do módulo de perfil.
#   É responsável pela manipulação dos dados do usuário logado do banco
#   de dados.
class IfPersProfile:
    __metaclass__ = ABCMeta

    ##  Função que recupera todos os dados do usuário.
    #       Percorre o banco de dados e recupera todos os dados do usuário
    #       requisitado.
    #
    #   @arg    username    Nome do usuário a ser pesquisado.
    #
    #   @arg    database    Objeto modelo sobre o qual a consulta será
    #                       realizada.
    @abstractmethod
    def fetch(self, username, database): pass

    ##  Método que atualiza os dados de um usuário fornecido.
    #       No caso de campos multivalorados, adiciona uma nova entrada.
    #       Caso contrário, substitui a entrada anterior.
    #
    #   @arg    username    Nome do usuário sobre o qual a consulta será
    #                       realizada.
    #   @arg    field       Campo a ser atualizado.
    #
    #   @arg    newdata     Dado a ser atualizado.
    #
    #   @arg    database    Objeto de modelo que será utilizado.
    @abstractmethod
    def update(self, username, field, newdata, database): pass

## Camada de apresentação para a página principal do site.
#   Deve carregar o devido template, contendo os dados básicos do usuário,
#   como cursos matriculados e histórico para estudantes, e cursos monitorados
#   para professores.
class UiHomeProfile(IfUiProfile): 

    def run(self, request):
        user = request.session['user']
        if not 'matric' in user:
            request.session['user'] = self.bus.refreshUser(request)
            user = request.session['user']
        translation.activate(request.session['user']['language'])
        return render(request, "Profile/home.html", {'user' : user})

## Camada de apresentação para a página de perfil completa.
#   Deve ser capaz de gerar uma página que disponibilize os dados
#   do usuário, permitindo que ele edite ou não, alguns campos.
#   Caso a run() seja chamada com um argumento adicional field,
#   a chamada será considerada assíncrona, assim como no caso do
#   request.method ser POST.
class UiFullProfile(IfUiProfile):

    ## Lista de campos passíveis de edição por um usuário.
    __editable = [
                    'interests',
                    'name',
                    'language',
                    'sex',
                    'bios',
                    'avatar'
                    ]
    __viewable = [
                    'email',
                    'campus',
                    'matric'
                    ]

    def __init__(self, bus):
        self.__viewable += self.__editable
        try:
            self.bus = bus
        except TypeError as exc:
            del self
            raise exc

    ##  Capaz de criar um template-iterable array com os dados de usuario.
    def __makeData(self, user):
        data = {}
        for field, value in user.items():
            if field in self.__viewable:
                data[field] = {
                    "value": value,
                    "edit":True if field in self.__editable else False,
                    "mult":True if isinstance(value, list)  else False,
                    "fname": lang.DICT[field.upper()],
                            }

        return data

    def run(self, request, field=None):

        get_user = lambda: request.session['user']

        ## @if Verifica qual o propósito do submit.
        #   Caso seja POST, a requisição ocorre após a submissão de uma form,
        #       muito provavelmente da form de edição de campo.
        #   Caso não seja, a requisição há de ser um GET, para mostrar as
        #       opções de edição.
        if request.method == "POST":

            try:
                if   "name" in request.POST:
                    form = NameForm(request.POST)
                    field = "name"
                elif "language" in request.POST:
                    form = LanguageForm(request.POST)
                    field = "language"
                elif "sex" in request.POST:
                    form = SexForm(request.POST)
                    field = "sex"
                elif "bios" in request.POST:
                    form = BiosForm(request.POST)
                    field = "bios"
                elif "interests" in request.POST:
                    form = InterestsForm(request.POST)
                    field = "interests"
                elif "avatar" in request.POST:
                    form = AvatarForm(request.POST, request.FILES)
                    field = "avatar"
                else:
                    raise ValueError(lang.DICT['EXCEPTION_INV_FRM'])

                if form.is_valid():
                    request.session['user'][field] = self.bus.editField(
                                                        request, 
                                                        field, 
                                                        form )
                    request.session.modified = True
                else:
                    raise ValueError(lang.DICT['EXCEPTION_INV_FRM'] + 
                        ":" + form.errors)

            except ValueError as exc:
                data = self.__makeData(get_user())
                return render(request, "Profile/full.html", {'data' : data,
                                                             'error': exc })

            data = self.__makeData(get_user())
            return HttpResponseRedirect('/profile')

        else: # request.method == "GET"
            if not field: # normal call
                request.session['user'] = self.bus.refreshUser(request)
                data = self.__makeData(get_user())
                return render(request, "Profile/full.html", {'data' : data})
            else: # ajax call
                err = False
                if   field == "name":
                    form = NameForm(initial={'newdata':get_user()['name']})
                    dlist = ""
                elif field == "language":
                    form = LanguageForm(initial={
                            'newdata':get_user()['language']})
                    dlist = ""
                elif field == "sex":
                    form = SexForm(initial={'newdata':get_user()['sex']})
                    dlist = ""
                elif field == "bios":
                    form = BiosForm(initial={'newdata':get_user()['bios']})
                    dlist = ""
                elif field == "interests":
                    form = InterestsForm(initial={
                            'newdata':get_user()['interests']})
                    dlist = self.bus.listInterests()
                elif field == "avatar":
                    form = AvatarForm()
                    dlist = ""
                else:
                    form = lang.DICT["ERROR_FORM"]
                    err = True 

                return render(request, "Profile/edit.html", {'form': form,
                                                             'ff': field,
                                                             'err': err,
                                                             'dlist': dlist })
        

## Camada de negócio para perfil.
#   Deve ser capaz de manipular os dados de usuário, seja no sentido de 
#   atualizá-los ou modificá-los de alguma forma.
class BusProfile(IfBusProfile):

    def refreshUser(self, request):
        user = request.session['user']
        if user['type'] == 'Student':
            fs = self.pers.fetch(user['name'], Student)
            fd = dict(fs)
            request.session['django_language'] = fd['language']
            return dict(user.items()+ self.pers.fetch(user['name'], Student))
        elif user['type'] == 'Professor':
            return dict(user.items()+ self.pers.fetch(user['name'], Professor))

    def editField(self, request, field, form):
        user = request.session['user']
        if field == "name":
            fpw = form.cleaned_data['password'].value
            if fpw != user['password']:
                raise ValueError(lang.DICT['EXCEPTION_INV_PW_F'])
            newdata = form.cleaned_data['newdata'].value
        elif field == "language":
            newdata = form.cleaned_data['newdata']
        elif field == "avatar":
            addr = settings.MEDIA_ROOT + u"/" + user['avatar']
            with open(addr, "wb+") as destination:
                    for chunk in request.FILES['newdata'].chunks():
                        print "UPLOADING FILE"
                        destination.write(chunk)
        else:
            newdata = form.cleaned_data['newdata'].value

        try:
            if user['type'] == 'Student' and field != 'avatar':
                self.pers.update(user['name'], field, newdata, Student)
            elif user['type'] == 'Professor' and field != 'avatar':
                self.pers.update(user['name'], field, newdata, Professor)
        except ValueError as exc:
            raise ValueError(lang.DICT['EXCEPTION_ERR_DB_U'])
        else:
            if field == "language":
                request.session['django_language'] = newdata
        if field == 'avatar':
            return user['avatar']
        else:
            return newdata

    def listInterests(self):
        return self.pers.fetchField("INTEREST")

## Camada de persistência de perfil.
#   Recupera os dados do usuário logado, retornando-os para a camada
#   de negócio.
class PersProfile(IfPersProfile):

    def __select_field(self, uid, field, database):

        try:
            ret = database.objects.get(identity=uid, field=field)
            ret = ret.value

        except database.MultipleObjectsReturned:
            ret = map(lambda x: x.value, database.objects.filter(
                    identity=uid, field=field))

        except database.DoesNotExist:
            ret = None 

        return ret

    def fetch(self, username, database):

        try:
            uid = database.objects.get(field='NAME',value=username)
            uid = uid.identity

            sf = lambda x: self.__select_field(uid, x, database)

            fetchset = [
                    ('password',    sf('PASSWORD')),
                    ('matric',      sf('MATRIC')),
                    ('bios',        sf('BIOS')),
                    ('campus',      sf('CAMPUS')),
                    ('courses',     sf('COURSE')),
                    ('avatar',      sf('AVATAR')),
                    ('email',       sf('EMAIL')),
                    ('sex',         sf('SEX')),
            ]

            if database is Student:
                fetchset = fetchset + [     
                    ('grades',      sf('GRADE')),
                    ('interests',   sf('INTEREST')),
                    ('language',    sf('LANGUAGE')),
                ]

        except database.DoesNotExist as exc:
            fetchset = []

        return fetchset

    def fetchField(self, field):

        ret = []

        try:
            lstu = Student.objects.filter(field=field)   #list of students
            lpro = Professor.objects.filter(field=field) #list of professors 

        except Student.DoesNotExist:
            lstu = []
        except Professor.DoesNotExist:
            lpro = []

        for s in lstu:
            ret.append(s.value)

        for p in lpro:
            ret.append(p.value)

        return ret

    def update(self, username, field, newdata, database):
        
        try:
            uid = database.objects.get(field='NAME', value=username)
            uid = uid.identity

            ## Para o caso de COURSEs, GRADEs ou INTERESTs.
            if field[-1] == 's':
                if field[-2] == 'e' or field[-2] == 't':
                    field = field[:-1]
                
            try:
                data = database.objects.get(field=field.upper(), identity=uid)
                data.value = newdata
            except database.DoesNotExist:
                data = database(identity=uid, field=field.upper(), value=newdata)
            data.save()

        except ( database.DoesNotExist, 
                 database.MultipleObjectsReturned ) as exc:
            raise ValueError(exc)

#coding: utf-8

from __future__ import division

## @file ProfileUnit.py
#   Este arquivo é responsável pelo armazenamento de todas as camadas 
# correspondentes ao módulo de perfil. 
#   O módulo de perfil é designado a administrar duas das páginas do site
# final: a página "home" e a página de perfil.
#   Na página Home, o usuário (Student ou Professor, Adms não possuem perfil)
# terá acesso a uma versão resumida do seu perfil, bem como um infográfico com
# o seu desenvolvimento nos cursos em que está cadastrado. É possível, a partir
# desta página, acessar a página de perfil e a página de curso (vide 
# CourseUnit.py).
#   A página de perfil, por sua vez, disponibilizará ao usuário (quase) todas
# as informações que o sistema guarda sobre ele, e também o possibilitará 
# editar alguns campos, como "interesses" ou "biografia".
# É nesta página que o usuário poderá alterar sua senha.

from abc import *

import ELO.locale.index as lang

from ELO.models import Student, Professor, Courses
from Profile.forms import (
    NameForm, 
    PasswordForm,
    LanguageForm,
    SexForm,
    BiosForm,
    InterestsForm,
    AvatarForm)

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import translation

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


    ## Método que recupera os dados de um campo específico de todos.
    #       Atualmente, não está sendo utilizado para nada, mas numa versão
    #       anterior do software, era capaz de recuperar os interesses dos
    #       usuários para listá-los e agrupá-los.
    #
    #   @arg    field       Campo a ser pesquisado.
    def fetchField(self, field): pass

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
                    'name',
                    'password',
                    'sex',
                    'bios',
                    'avatar'
                    ]

    __editable_stu = [
                    'language',
                    'interests'
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

        if user["type"] == "Student":
            self.__viewable += self.__editable_stu
            __ed = self.__editable + self.__editable_stu
        else:
            __ed = self.__editable

        for field, value in user.items():
            if field in self.__viewable:
                data[field] = {
                    "value": value,
                    "edit":True if field in __ed else False,
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
                if  "password" in request.POST:
                    form = PasswordForm(request.POST)
                    field = "password"
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
                    raise ValueError(lang.DICT['EXCEPTION_INV_FRM'])

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
                l = request.session['user']['language']
                translation.activate(l)
                request.session[translation.LANGUAGE_SESSION_KEY] = l
                return render(request, "Profile/full.html", {'data' : data})
            else: # ajax call
                err = False
                if   field == "name":
                    form = NameForm(initial={'newdata':get_user()['name']})
                elif field == "password":
                    form = PasswordForm()
                elif field == "language":
                    form = LanguageForm(initial={
                            'newdata':get_user()['language']})
                elif field == "sex":
                    form = SexForm(initial={'newdata':get_user()['sex']})
                elif field == "bios":
                    form = BiosForm(initial={'newdata':get_user()['bios']})
                elif field == "interests":
                    form = InterestsForm(initial={
                            'newdata':get_user()['interests']})
                elif field == "avatar":
                    form = AvatarForm()
                else:
                    form = lang.DICT["ERROR_FORM"]
                    err = True 

                return render(request, "Profile/edit.html", {'form': form,
                                                             'ff': field,
                                                             'err': err,
                                                            })
        

## Camada de negócio para perfil.
#   Deve ser capaz de manipular os dados de usuário, seja no sentido de 
#   atualizá-los ou modificá-los de alguma forma.
class BusProfile(IfBusProfile):

    def refreshUser(self, request):
        user = request.session['user']

        if user['type'] == 'Student':
            db = Student
        elif user['type'] == 'Professor':
            db = Professor

        fs = self.pers.fetch(user['name'], db)
        fd = dict(fs)
        request.session['django_language'] = fd['language']
        return dict(user.items() + fs)

    def editField(self, request, field, form):
        user = request.session['user']
        if field == "name":
            fpw = form.cleaned_data['password'].value
            if fpw != user['password']:
                raise ValueError(lang.DICT['EXCEPTION_INV_PW_F'])
            newdata = form.cleaned_data['newdata'].value
        elif field == "password":
            npw = form.cleaned_data['newdata'].value
            rpw = form.cleaned_data['rp_newdata'].value
            opw = form.cleaned_data['old_password'].value
            if npw != rpw:
                raise ValueError(lang.DICT['EXCEPTION_INV_PW_R'])
            if opw != user['password']:
                raise ValueError(lang.DICt['EXCEPTION_INV_PW_F'])
            newdata = npw
        elif field == "language":
            newdata = form.cleaned_data['newdata']
        elif field == "avatar":
            addr = settings.MEDIA_ROOT + u"/" + user['avatar']
            with open(addr, "wb") as destination:
                    for chunk in request.FILES['newdata'].chunks():
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
                    ('avatar',      sf('AVATAR')),
                    ('email',       sf('EMAIL')),
                    ('sex',         sf('SEX')),
                    ('language',    sf('LANGUAGE')),
            ]

            sfc = sf('COURSE') # select field courses

            if database is Student:
                fetchset = fetchset + [     
                    ('grades',      sf('GRADE')),
                    ('interests',   sf('INTEREST'))
                ]

                sfmc = sf('MODULE_COMPLETED') # Set Fetch for modules completed
                lc = [] # List of courses
                
                for c in sfc:
                    nmod = Courses.objects.filter(identity=c,
                                                  field='MODULE').count()

                    # Get number of modules completed
                    sfmc = 1 if not sfmc is list else sfmc.length()

                    cname = Courses.objects.get(identity=c, field='NAME').value
                    lc = lc + [({'name':cname, 'id':c}, sfmc*100/nmod)]

                sfc = lc

            fetchset = fetchset + [('courses', sfc)]

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

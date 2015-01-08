#coding: utf-8

## @file Armazenamento de todas as camadas correspondentes ao módulo de login.
#   Os métodos aqui são criados e chamados pela Factory (MainUnit.py) quando
#   necessários.
#   Eles são responsáveis pela criação, gestão e deleção do objeto de sessão e 
#   validação e login dos usuários.

from abc import *

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.template import Template, Context
from django.utils import translation
from django import forms

from ELO.models import Student, Adm, Professor
from ELO.BaseUnit import Name, Password
from Login.forms import LoginForm

import ELO.locale.index as lang

## Interface para a camada de Apresentação de Usuário do módulo Login.
#   É responsável pelo carregamento do template correto e processa os dados
#   inseridos no formulário de login.
class IfUiLogin:
    ## Força a criação da camada subjacente
    __metaclass__ = ABCMeta

    def __init__(self, bus):
        try:
            self.bus = bus
        except TypeError as exc:
            del self
            raise exc

    ## Objeto que representa a camada de negócio, subjacente a de UI.
    #   Deve ser inicializada no momento da criação de um objeto do tipo
    #   UiLogin, ou seja, uma camada de UI nunca existirá sem uma camada
    #   de Bus suportando-a.
    @property
    def bus(self):
        return self.__bus

    @bus.setter
    def bus(self, value):
        if isinstance(value, IfBusLogin):
            self.__bus = value
        else:
            raise TypeError("Expected IfBusLogin instance at \
                    UiLogin.__bus. Received " + str(type(value)) + " instead.")

    ## Método de deleção do objeto que representa a camada de negócio.
    @bus.deleter
    def bus(self):
        del self.__bus

    ## O método principal de qualquer classe de UI (user interface), o método
    #   run() permite à Factory dar o controle do programa ao módulo de Login.
    @abstractmethod
    def run(self, request): pass


## Interface para a camada de negócio do módulo de Login.
#   Responsável pela validação dos dados submetidos através do formulário de
#   login.
class IfBusLogin: 
    __metaclas__ = ABCMeta

    ## Método de validação.
    #   Não deve retornar nada, mas lança uma exceção do tipo ValueError no
    #   caso de uma validação mal-sucedida.
    #
    #   @arg username   Nome do usuário a ser validado.
    #
    #   @arg password   Senha a ser validada, junto ao username.
    #
    #   @arg database   Classe do modelo a ser utilizado.
    @abstractmethod
    def validate(self, username, password, database): pass


    ## Método de recuperação de linguagem de sistema.
    #   Retorna uma string com o código da linguagem preferida pelo usuário.
    #
    #   @arg username   Nome do usuário a ser verificado.
    #
    #   @arg database   Classe do modelo a ser utilizado.
    @abstractmethod
    def getLang(self, username, database): pass

    @property
    def pers(self):
        return self.__pers

    @pers.setter
    def pers(self, pers):
        if isinstance(value, IfPersLogin):
            self.__pers = pers
        else:
            raise TypeError("Expected IfPersLogin instance at \
                BusLogin.__pers. Received " + str(type(value)) + "instead.")

    ## Método de deleção do objeto que representa a camada de persistência.
    @pers.deleter
    def pers(self):
        del self.__pers

    ## Força a criação da camada subjacente.
    def __init__(self, value):
        try:
            self.pers = value
        except TypeError as exc:
            del self
            raise exc


## Interface para a camada de persistência do módulo de Login.
#   Deve ser capaz de capturar os dados necessários do banco de dados.
class IfPersLogin:

    __metaclass__ = ABCMeta

    ## Retorna um dicionário no formato de objeto com os dados do usuário
    #   requisitado.
    @abstractmethod
    def select(self, username, database): pass


## Camada de interface de usuário para o módulo de Login.
class UiLogin(IfUiLogin):

    ## Método que inicia o módulo de login. 
    #   Aqui, ocorre a validação de formulário, autenticação de usuário, e
    #   redirecionamento para a página de perfil.
    def run(self, request, database):
        if request.method == "POST":
            login_form = LoginForm(request.POST)
            try: 
                if login_form.is_valid():
                    self.bus.validate(login_form.cleaned_data['username'],
                        login_form.cleaned_data['password'], database)
                else:
                    raise ValueError(lang.DICT['EXCEPTION_INV_LOG'])
            except ValueError as exc:
                if database.__name__ == "Professor":
                    target = "proflogin"
                elif database.__name__ == "Adm":
                    target = "364fd8cdc3a35a89b7be75bc9d10ebea"
                elif database.__name__ == "God":
                    target = "e50b058759a52eda8a507687887186e5"
                else:
                    target = ""

                return render(request, "Login/form.html", {'form': login_form, 
                    'error': exc, 'target': target})
            else:
                l = None
                cd = login_form.cleaned_data
                if (database.__name__ != "Adm" and
                    database.__name__ != "God"):
                    l = self.bus.getLang(cd['username'], database)
                else:
                    l = request.LANGUAGE_CODE
                request.session['user'] = {
                                'name': cd['username'].value,
                                'password': cd['password'].value,
                                'language': l ,
                                'type': database.__name__,
                            }
                translation.activate(l)
                request.session[translation.LANGUAGE_SESSION_KEY] = l
                return HttpResponseRedirect('/')
        else:
            login_form = LoginForm()

            if not database:
                target = ""
            if database.__name__ == "Professor":
                target = "proflogin"
            elif database.__name__ == "Adm":
                target = "364fd8cdc3a35a89b7be75bc9d10ebea"
            elif database.__name__ == "God":
                target = "e50b058759a52eda8a507687887186e5"
            else:
                target = ""

            return render(request, "Login/form.html", 
                {'form': login_form, 'target': target})


## Camada de negócio de usuário para o módulo de Login.
class BusLogin(IfBusLogin):

    def validate(self, username, password, database):
        upass = self.pers.select(username.value, database)
        if not upass or upass['password'] != password.value:
            raise ValueError(lang.DICT['EXCEPTION_INV_LOG'])

    def getLang(self, username, database):
        ulang = self.pers.select(username.value, database)
        return ulang['language']

## Camada de persistência de usuário para o módulo de Login.
class PersLogin(IfPersLogin):

    def select(self, username=None, database=None):
        if not username: return False
        if not database: return False

        upass = None
        ulang = None

        if database.__name__ == "God":
            try:
                usr = database.objects.get()
            except database.DoesNotExist:
                return False
            except database.MultipleObjectsReturned:
                return False

            username = usr.username
            upass = usr.password
        else:

            try:
                uid = database.objects.get(value=username, field='NAME')
                uid = uid.identity
                upass = database.objects.get(identity=uid, field='PASSWORD')
                upass = upass.value
            except database.DoesNotExist:
                return False

            if(database.__name__ == "Student" or 
               database.__name__ == "Professor"):
                try:
                    ulang= database.objects.get(identity=uid, field='LANGUAGE')
                    ulang= ulang.value
                except database.DoesNotExist:
                    return False
            else:
                ulang = settings.LANGUAGE_CODE

        return { 'name': username, 'password': upass, 'language': ulang }

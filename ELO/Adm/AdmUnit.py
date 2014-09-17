#coding: utf-8

## @file AdmUnit.py
#   Este arquivo é responsável pelo armazenamento de todas as camadas correspondentes 
#   ao módulo de administrador. 
#   Os métodos aqui são criados e chamados pela Factory (MainUnit.py) quando necessários. 
#   São responsáveis por cadastrar, deletar e editar alunos e professores 
#   no banco de dados, criar cursos e ver um log sobre os últimos eventos no sistema.

from abc import *

import ELO.locale.index as lang

from ELO.models import Adm, Student, Professor
from forms import *
from Profile.forms import (
    NameForm, 
    LanguageForm,
    SexForm,
    BiosForm,
    InterestsForm,
    AvatarForm)

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django import forms

## Interface para a camada de apresentação de Usuário do módulo de Administração.
#   É responsável pelo carregamento do template correto e processa os dados
#   inseridos no formulário de Administração.
class IfUiAdm:
    __metaclass__ = ABCMeta
    
    # Construtor da classe.
    #   Força a criação da camada subjacente.
    def __init__(self, bus):
        try:
            self.bus = bus
        except TypeError as exc:
            del self
            raise exc

    ## Objeto que representa a camada de negócio, subjacente a de UI.
    #   Deve ser inicializada no momento da criação de um objeto do tipo
    #   UiAdm, ou seja, uma camada de UI nunca existirá sem uma camada
    #   de Bus suportando-a.
    @property
    def bus(self):
        return self.__bus

    ## Checa se o objeto recebido é uma instância do Business.
    #   Caso contrário, ele emite um erro de tipo, explicitando
    #   qual tipo do objeto que foi recebido.
    @bus.setter
    def bus(self, value):
        if isinstance(value, IfBusAdm):
            self.__bus = value
        else:
            raise TypeError("Expected IfBusAdm instance at \
                UiAdm.__bus. Received " + str(type(value)) + " instead.")

    ## Método de deleção do objeto que representa a camada de negócio.
    @bus.deleter
    def bus(self):
        del self.__bus

    ## O método principal de qualquer classe de UI (User Interface).
    #   O método run() permite à Factory dar o controle do programa 
    #   ao módulo de Administração.
    @abstractmethod
    def run(self, request, action=None, model=None): pass

## Interface para a camada de negócio do módulo de Administração.
#   É responsável pela validação dos dados submetidos através do 
#   formulário de Administração.
class IfBusAdm:
    __metaclass__ = ABCMeta

    ## Construtor da classe.
    #   Força a criação da camada subjacente.
    def __init__(self, pers):
        try:
            self.pers = pers
        except TypeError as exc:
            del self
            raise exc
    
    ## Objeto que representa a camada de persistência, subjacente a de Bus.
    #   Deve ser inicializada no momento da criação de um objeto do tipo
    #   BusAdm, ou seja, uma camada de Bus nunca existirá sem uma camada
    #   de Pers suportando-a.
    @property
    def pers(self):
        return self.__pers

    ## Checa se o objeto recebido é uma instância da Persistência.
    #   Caso contrário, ele emite um erro de tipo, explicitando
    #   qual tipo do objeto que foi recebido.
    @pers.setter
    def pers(self, value):
        if isinstance(value, IfPersAdm):
            self.__pers = value
        else:
            raise TypeError("Expected IfPersAdm instance at \
                BusAdm.__pers. Received " + str(type(value)) + " instead.")

    ## Método de deleção do objeto que representa a camada de persistência.
    @pers.deleter   
    def pers(self):
        del self.__pers

    ## Edita dados de um conta no database.
    #   Podendo ser este de uma conta de Estudante, Professor ou um Curso.
    #
    #   @arg field      Nome do objeto a ser registrado.
    #
    #   @arg form       Objeto form que contém os dados.
    @abstractmethod
    def editAccounts(self, request, field, form): pass

    ## Verifica os últimos eventos realizados pelo Administrador.
    #@abstractmethod
    #def checkEvents(self, request): pass
    

## Interface para a camada de persistência do módulo de Administração.
#   É responsável pela manipulação dos dados do sistema do banco
#   de dados.
class IfPersAdm:
    __metaclass__ = ABCMeta

    ## Insere os dados do registro de contas no banco de dados.
    #   Contas dos tipos Estudantes e Professores, e cursos.
    #
    #   @arg    dict_field  Dicionário de campos ligados a valores.
    #
    #   @arg    database    Objeto modelo sobre o qual a inserção será
    #                       realizada (Estudante, Professor, Curso). 
    @abstractmethod
    def data_in(self, dict_field_value, database): pass

    ## Método que atualiza os dados de uma conta fornecida.
    #   No caso de campos multivalorados, adiciona uma nova entrada.
    #   Caso contrário, substitui a entrada anterior.
    #   É necessário a senha do administrador para que
    #   essa operação possa ser executada.
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

    ## Método que deleta os dados de uma conta fornecida.
    #   É necessário a senha do administrador para que
    #   essa operação possa ser executada.
    #
    #   @arg    username    Nome da conta a ser deletada.
    #
    #   @arg    database    Objeto modelo sobre o qual a consulta será
    #                       realizada.
    @abstractmethod
    def fetch_del(self, username, database): pass

## Camada de interface do Administrador para o módulo de Administração.
#   Deve carregar o devido template, contendo campos onde será
#   permitido a criação, edição e deleção de contas do tipo Estudante,
#   Professor e Cursos.
#   Caso seja feito o pedido de alteração em qualquer condição
#   citada acima então será chamada uma caixa com formulários
#   requisitando os devidos dados necessários de cada ação.
class UiAdm(IfUiAdm): 

    ## O método principal de qualquer classe de UI (User Interface).
    def run(self, request, action=None, model=None):
        # Coleta o usuario da sessão atual
        get_user = lambda: request.session['user']

        ## @if Verifica qual o propósito do submit.
        #   Caso seja POST, a requisição ocorre após a submissão de uma form,
        #       podendo ser ela de registro, edição ou deleção.
        #   Caso não seja e não ocorra a passagem dos campos de ação e modelo,
        #       a requisição há de ser um GET, para mostrar a página principal de Adm.
        #   Em último caso será a requisição do Javascript, denominada como AJAX,
        #       que irá solicitar em tempo de eventos dos dialogs iniciados,
        #       dados para requisição dos forms adequados e informações
        #       do usuário procurado para uma possível edição ou deleção.


        # Se a requisição for por meio de POST ela coleta o dicionário de fields ligados
        #   aos novos dados e chama as funções adequadas de edição.
        if request.method == "POST":
            return render(request, "Adm/edit.html")
        # Quando a requisição for de GET então é retornado para a página principal.                                            })
        else:
            # Chamada normal de GET.
            if ((not action) and (not model)):
                return render(request, "Adm/home.html")
            # Caso contrário, no caso de requisições do tipo AJAX, 
            #   irá ser repassado forms adequados ao pedido ou será feito
            #   buscas de dados do usuário atual.
            else:
                return render(request, "Adm/edit.html")




## Camada de negócio para o módulo de administração.
#   Deve ser capaz de manipular os dados do sistema,
#   dando as devidas diretrizes ao banco de dados para que seja
#   inserido, atualizado ou deletado dados sobre uma determinada
#   conta, podendo ser esta de um Estudante, Professor ou de um Curso.
class BusAdm(IfBusAdm): 

    ## Edita dados de um conta no database.
    #   Podendo ser este de uma conta de Estudante, Professor ou um Curso.
    def editAccounts(self, request, field, form): pass

## Camada de persistência para o módulo de administração.
#   Recupera os dados do banco de dados referentes aos alunos
#   professores e cursos, retornando-os para a camada de negócio.
class PersAdm(IfPersAdm):

    ## Insere os dados do registro de contas no banco de dados.
    def data_in(self, dict_field_value, database):
        # Tenta coletar o último id inserido.
        # Caso não tenha ocorrido nenhum registro de contas então
        # é atribuído o valor inicial como '1'
        try:
            # Coleta o ultimo ID inserido no identity do database.
            lastid = database.objects.order_by('-identity')[0]
            # Newid será a identity do novo usuário.
            newid = lastid.identity + 1
        except IndexError:
            newid = 1
        
        # Percorre o dicionário ligado aos campos a seu valores.
        for fields in dict_field_value:
            # Insere novos dados: identidade, campo e a novo valor.
            data = database(identity=newid, field=fields.upper(),
                             value=dict_field_value[fields])
            # Salva os novos dados no database.
            data.save()

    ## Método que atualiza os dados de uma conta fornecida.
    def update(self, username, field, newdata, database): 
        # Tenta procurar se o username existe no banco de dados.
        # Caso não exista, é emitido um erro.
        try:
            # Filtra o database pelo nome do usuario.
            uid = database.objects.get(field='NAME', value=username)
            # Coleta a ID do usuário encontrado.
            uid = uid.identity
                
            try:
                # Coleta a partir do ID do usuário o valor do campo
                # que deseja atualizar.
                data = database.objects.get(identity=uid, field=field.upper())
                # Nova informação é colocada no tipo que deseja atualizar.
                data.value = newdata
            # Caso o novo valor a ser colocado já exista então este continua o mesmo.
            except database.DoesNotExist:
                data = database(identity=uid, field=field.upper(), value=newdata)
            # Salva os novos dados no database.
            data.save()

        except ( database.DoesNotExist, 
                 database.MultipleObjectsReturned ) as exc:
            raise ValueError(exc)

    ## Método que deleta os dados de uma conta fornecida.
    def fetch_del(self, username, database):
        # Tenta procurar se o username existe no banco de dados.
        # Caso não exista, é emitido um erro.
        try:
            # Filtra o database pelo nome do usuario.
            uid = database.objects.get(field='NAME',value=username)
            # Coleta a ID do usuário
            uid = uid.identity

        # Caso usuário não exista, então é retornado para o Business
        # que não foi encontrado.
        except database.DoesNotExist:
            return False

        # Tenta filtrar os dados de um ID.
        # Caso não exista, é emitido um erro.
        try:   
            # Lista da filtragem dos dados de um determinado ID.
            accdel = database.objects.filter(identity=uid)
            # Lista dos dados é deletada do database.
            accdel.delete()
       
        except ( database.DoesNotExist, 
                database.MultipleObjectsReturned ) as exc:
            raise ValueError(exc)

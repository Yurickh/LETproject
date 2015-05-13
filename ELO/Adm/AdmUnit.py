#coding: utf-8

## TODO:
#   Implementar log de eventos que o Adm ou God realizar.
#   Conf. com senha adm para todas ações.
#   Courses visualizar alunos.

## @file AdmUnit.py
#   Este arquivo é responsável pelo armazenamento de todas as camadas 
#   correspondentes ao módulo de administrador. 
#   Os métodos aqui são criados e chamados pela Factory (MainUnit.py)
#   quando necessários. 
#   São responsáveis por cadastrar, deletar e editar alunos e professores 
#   no banco de dados, criar cursos e ver um log sobre os últimos eventos no
#   sistema.

from abc import *

import ELO.locale.index as lang

import django_tables2 as tables
from django_tables2   import RequestConfig

from ELO.models import Adm, Student, Professor, Tutor, Courses, God, Identities

from forms import (
    RegUserForm,
    RegAdmForm,
    SrcUserForm,
    ConfAdmForm,
    RegCourForm,
    SrcCourForm,
    EditUserForm,
    EditCourForm,
    EditAdmForm)

from tables_models import StudentTable, ProfessorTable, CoursesTable

from Profile.forms import (
    NameForm, 
    PasswordForm,
    LanguageForm,
    SexForm,
    BiosForm,
    InterestsForm,
    AvatarForm)

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django import forms

HOME_ACCOUNTS = 'Adm/adm_accounts.html'
NEW_ACCOUNTS = "Adm/new_acc.html"
EDIT_ACCOUNTS = "Adm/edit_acc.html"
DEL_ACCOUNT = "Adm/del_acc.html"
STUDENTS = 'students'
PROFESSORS = 'professors'
TUTORS = 'tutors'
COURSES = 'courses'
ADM = 'adms'
GOD = 'God'
SEARCH = 'search'
REGISTER = 'register'
DELETE = 'delete'
EDIT = 'edit'
NAME = 'nome'
POST = 'POST'
ACTION = 'act'

## Interface para a camada de apresentação de Usuário do módulo de Adm.
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
    def run(self, request, model=None, username=None, action=None): pass

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

    @abstractmethod
    def allAccounts(self, model): pass

    ## Cria uma conta no database.
    #   Podendo ser esta uma conta de Estudante, Professor ou um Curso.
    #   
    #   @arg    form    Valores dos campos para registro validados.
    #
    @abstractmethod
    def regAccount(self, request, form): pass

    ## Deleta uma conta no database.
    #   Podendo ser esta uma conta de Estudante, Professor ou um Curso.
    @abstractmethod
    def delAccount(self, request): pass

    @abstractmethod
    def editAccount(self, request): pass

    ## Procura conta do database.
    #   Podendo ser esta uma conta de Estudante, Professor ou um Curso.
    #
    #   @return data    Dados da conta procurada.
    @abstractmethod
    def fetchAccount(self, model, request=None, accountid=None): pass

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
    def dataIn(self, dict_field_value, database): pass

    ## Método que deleta os dados de uma conta fornecida.
    #   É necessário a senha do administrador para que
    #   essa operação possa ser executada.
    #
    #   @arg    username    Nome da conta a ser deletada.
    #
    #   @arg    database    Objeto modelo sobre o qual a consulta será
    #                       realizada.
    @abstractmethod
    def fetchDelUser(self, username, database): pass

    ## Método que deleta os dados de um curso fornecida.
    #   É necessário a senha do administrador para que
    #   essa operação possa ser executada.
    #
    #   @arg    courMatric    Matrícula da conta a ser deletada.
    #
    #   @arg    database    Objeto modelo sobre o qual a consulta será
    #                       realizada.
    @abstractmethod
    def fetchDelCour(self, courMatric, database): pass

    ##  Função que recupera todos os dados de um usuário pesquisado.
    #
    #   @arg    username    Nome do usuário a ser pesquisado.
    #
    #   @arg    database    Objeto modelo sobre o qual a consulta será
    #                       realizada.
    #
    #   @return fetchset    Lista com tuplas dos campos e valores do curso.
    @abstractmethod
    def fetchUser(self, username, database): pass

    ##  Função que recupera todos os dados de um curso pesquisado.
    #
    #   @arg    courMatric  Número da matrícula do Curso a ser pesquisado.
    #
    #   @arg    database    Objeto modelo sobre o qual a consulta será
    #                       realizada.
    #
    #   @return fetchset    Lista com tuplas dos campos e valores do curso.
    @abstractmethod
    def fetchCour(self, courMatric, database): pass

    @abstractmethod
    def fetchAllUser(self, database): pass

    @abstractmethod
    def fetchAllCour(self, database): pass

    @abstractmethod
    def editUser(self, request, database): pass

    @abstractmethod
    def editCour(self, request, database): pass

## Camada de interface do Administrador para o módulo de Administração.
#   Deve carregar o devido template, contendo campos onde será
#   permitido a criação, edição e deleção de contas do tipo Estudante,
#   Professor e Cursos.
#   Caso seja feito o pedido de alteração em qualquer condição
#   citada acima então será chamada uma caixa com formulários
#   requisitando os devidos dados necessários de cada ação.
class UiAdm(IfUiAdm): 

    def __make_table(self, model, data, order=None):
        if model == STUDENTS:
            table = StudentTable(data)
        elif model == PROFESSORS or model == TUTORS or model == ADM:
            table = ProfessorTable(data)
        elif model == COURSES:
            table = CoursesTable(data)

        if order:
            table.order_by = order

        return table

    def run(self, request, model=None, username=None, action=None):
        ## @if Verifica qual o propósito do submit.
        #
        #   Caso seja POST, a requisição ocorre após a submissão de uma form,
        #   podendo ser ela de registro, edição ou deleção.
        #
        #   Caso não seja e não ocorra a passagem dos campos de ação e modelo,
        #   a requisição há de ser um GET, para mostrar a página principal
        #   de Adm.
        #
        #   Em último caso será a requisição do Javascript, denominada como 
        #   AJAX, que irá solicitar em tempo de evento dos dialogs 
        #   iniciados. Será passada informações para requisitar os forms
        #   adequados e informações do usuário procurado para uma possível
        #   edição ou deleção.
        if request.method == POST:
            if model == COURSES:
                form_search = SrcCourForm()
            else:
                form_search = SrcUserForm()

            data = None
            exc = False
            try:
                if model == ADM and request.session['user']['type'] != GOD:
                    raise ValueError(lang.DICT['ERROR_MODEL'])

                if ACTION in request.POST:
                    if action == SEARCH:
                        if model == COURSES:
                            search_form = SrcCourForm(request.POST)
                        else:
                            search_form = SrcUserForm(request.POST)

                        if search_form.is_valid():

                            dacc = self.bus.fetchAccount(model, request)

                            data = [{'NAME':dacc[0]['NAME']}]

                            if model != COURSES:
                                data[0]['EMAIL'] = dacc[0]['EMAIL']

                                if model == STUDENTS:
                                    data[0]['MATRIC'] = dacc[0]['MATRIC']
                            else:
                                data[0]['COURMATRIC'] = dacc[0]['COURMATRIC']
                                data[0]['PROFESSOR'] = dacc[0]['PROFESSOR']
                            print data
                        else:
                            raise ValueError(lang.DICT['EXCEPTION_INV_FRM'])

                    elif action == REGISTER:
                        if model == COURSES:
                            reg_form = RegCourForm(request.POST)
                        elif model == ADM:
                            reg_form = RegAdmForm(request.POST)
                        else:
                            reg_form = RegUserForm(request.POST)

                        if reg_form.is_valid():
                            self.bus.regAccount(request, reg_form)
                        else:
                            raise ValueError(lang.DICT['EXCEPTION_INV_FRM'])

                    elif action == DELETE:
                        if model == COURSES:
                            delete_form = SrcCourForm(request.POST)
                        else:
                            delete_form = SrcUserForm(request.POST)

                        if delete_form.is_valid():
                            self.bus.delAccount(request)
                        else:
                            raise ValueError(lang.DICT['EXCEPTION_INV_FRM'])

                    elif action == EDIT:
                        if model == COURSES:
                            edit_form = EditCourForm(request.POST)
                        elif model == ADM:
                            edit_form = EditAdmForm(request.POST)
                        else:
                            edit_form = EditUserForm(request.POST)

                        if edit_form.is_valid():
                            self.bus.editAccount(request)                            
                        else:
                            raise ValueError(lang.DICT['EXCEPTION_INV_FRM'])
                    else:
                        raise ValueError(lang.DICT['EXCEPTION_404_ERR'])

            except ValueError as exce:
                exc = exce

            if not data:
                data = self.bus.allAccounts(model)

            table = self.__make_table(model, data, NAME)
            RequestConfig(request, paginate={"per_page": 
                                            25}).configure(table)

            return render(request, HOME_ACCOUNTS, 
                        {'form': form_search, 'data':table, 'err': exc,
                        'model':model,})


        elif not (model or username): #request.method == "GET"
            return render(request, "Adm/home.html", {"role": \
                                            request.session['user']['type']})
        else: #request.method == "AJAX"
            model1 = model[0]
            model3 = model[3:]
            exc = False

            if model1 == "s":
                model = model3
                URL = HOME_ACCOUNTS

                if model == COURSES:
                    form = SrcCourForm()
                else:
                    form = SrcUserForm()        

            elif model1 == "n":
                model = model3
                URL = NEW_ACCOUNTS

                if model ==COURSES:
                    form = RegCourForm()
                elif model == ADM:
                    form = RegAdmForm()
                else:
                    form = RegUserForm()                

            elif model1 == "d":
                model = model3
                URL = DEL_ACCOUNT

                if model == COURSES:
                    form = SrcCourForm()
                else:
                    form = SrcUserForm()

            elif model1 == "e":
                model = model[4:]
                URL = EDIT_ACCOUNTS
                acc = self.bus.fetchAccount(model, None, username)

                if model == COURSES:
                    form = EditCourForm(initial = \
                                        {'courMatric':acc[0]['COURMATRIC'], 
                                        'courName':acc[0]['NAME'],
                                        'courProfessor': acc[0]['PROFESSOR']})
                elif model == ADM:
                    form = EditAdmForm(initial = {'username':acc[0]['NAME'], 
                                                'userEmail': acc[0]['EMAIL']})
                else:
                    form = EditUserForm(initial = {'username':acc[0]['NAME'], 
                                                'userMatric':acc[0]['MATRIC'],
                                                'userCampus': acc[0]['CAMPUS'], 
                                                'userSex': acc[0]['SEX'], 
                                                'userEmail': acc[0]['EMAIL']})
            else:
                URL = HOME_ACCOUNTS
                exc = True
            
            data = self.bus.allAccounts(model)
            table = self.__make_table(model, data, NAME)
            RequestConfig(request, paginate={"per_page": 25}).configure(table)

            return render(request, URL, 
                        {'form': form, 'data': table, 'err': exc,
                         'model':model,})
                    

## Camada de negócio para o módulo de administração.
#   Deve ser capaz de manipular os dados do sistema,
#   dando as devidas diretrizes ao banco de dados para que seja
#   inserido, atualizado ou deletado dados sobre uma determinada
#   conta, podendo ser esta de um Estudante, Professor ou de um Curso.
class BusAdm(IfBusAdm): 

    def __check_db(self, model):
        if model == STUDENTS:
            db = Student
        elif model == PROFESSORS:
            db = Professor
        elif model == TUTORS:
            db = Tutor
        elif model == COURSES:
            db = Courses 
        elif model == ADM:
            db = Adm
        else:
            db = None
            raise ValueError(lang.DICT['ERROR_MODEL'])

        return db


    def allAccounts(self, model):
        db = self.__check_db(model)

        if db == Courses:
            data = self.pers.fetchAllCour(db) 
        else:
            data = self.pers.fetchAllUser(db)

        return data

    def regAccount(self, request, form):
        # Inicia o dicionário dict_data. 
        #   Será utilizado para informar os campos e dados para registro
        #   do usuário.
        dict_data = {}
        # Possíveis campos valorados dos modelos de contas.
        database_fields = ['NAME', 'SEX', 'PASSWORD', 'MATRIC', 
                           'CAMPUS','EMAIL', 'PROFESSOR']

        ## Percorre a requisição procurando os dados inseridos para registro.
        #   Se algum valor do campo não for válido então irá emitir erro de
        #   formulário inválido.
        for field, value in request.POST.items():
            # Transforma campo unicode em string.
            field = str(field)
            # Coleta a palavra chave do campo designado.
            # Esta é coletada a partir dos campos contidos 
            # no dicionário.
            newField = field[4:].upper()

            # Se o campo encontrado pertence à lista de campos
            # do database que deveriam pertencer a um usuário,
            # então este é adicionado ao dicionário que será 
            # repassado para inserção no banco de dados 
            # posteriormente.
            if newField in database_fields:
                dict_data[newField] = form.cleaned_data[field].value

        ## Verifica qual e o tipo do modelo requisitado para inserção 
        #   de nova conta.
        #    
        #   Caso a requisição venha com outro modelo não especificado nos
        #   condicionais então é emitido erro.

        model = str(request.POST['model'])

        db = self.__check_db(model)

        ## @if Verifica se a requisição pede outro modelo diferente de 
        #       Curso.
        #       
        #   Caso não for do modelo de Curso então é adionado a linguagem
        #   com valor default de Português.
        if model != COURSES:
            # Escolhe uma linguagem padrão para cadastro do usuário 
            # recente.
            dict_data['LANGUAGE'] = 'pt-br'

            result = self.pers.fetchUser(request.POST['username'], db)
        else:
            result = self.pers.fetchCour(request.POST['courMatric'], db)

        if not result:
            # É passado o dicionário de campos e valores do novo registro, e
            # o modelo de conta requisitado para criação destas informações 
            # no banco de dados (Persistência).
            self.pers.dataIn(dict_data, db)
        else:
            raise ValueError("Usuário já existe.")
        
    def delAccount(self, request):

        model = str(request.POST['model'])

        db = self.__check_db(model)

        try:
            if db == Courses:
                data = self.pers.fetchDelCour(str(request.POST['courMatric']), db)  
            else:
                data = self.pers.fetchDelUser(request.POST['username'], db) 

        except ValueError as exc:
            raise ValueError(exc)

        return data

    def editAccount(self, request):

        model = str(request.POST['model'])

        db = self.__check_db(model)

        try:
            if db == Courses:
                data = self.pers.editCour(request.POST, db)
            else:
                data = self.pers.editUser(request.POST, db) 

        except ValueError as exc:
            raise ValueError(exc)

        return data

    def fetchAccount(self, model, request=None, accountid=None):
        db = self.__check_db(model)


        if accountid == None:
            ## @if Confere se o modelo da Conta é um Curso.
            #
            #   Caso seja um curso é necessário passar a matrícula do Curso 
            #   como chave de busca de informações.
            #
            #   Caso contrário, é passado o username da conta de Estudante ou 
            #   de Professor.
            if db == Courses:
                data = self.pers.fetchCour(str(request.POST['courMatric']), db)  
            else:
                data = self.pers.fetchUser(str(request.POST['username']), db)
        else:
            if db == Courses:
                data = self.pers.fetchCour(accountid, db)  
            else:
                data = self.pers.fetchUser(accountid, db)
    

        ## @if Confere se foi retornado algo do banco de dados.
        #
        #   Caso não tenha sido retornado então é porque conta não existe.
        #
        #   Caso contrário é retornado as informações da conta.
        if not data:
            raise ValueError(lang.DICT['EXCEPTION_INV_USR_NM'])
        else:
            return data

class PersAdm(IfPersAdm):

    ## Seleciona campo a partir da identidade do usuário.
    #   Podendo ser estes de uma conta de Estudante, Professor ou um Curso.  
    #
    #   @arg    uid         Identidade de uma conta.
    #
    #   @arg    field       Objeto modelo sobre o qual a consulta será
    #                       realizada. 
    #
    #   @arg    database    Modelo de uma conta.   
    #
    #   @return ret         Valor do campo de alguma conta.
    def __select_field(self, uid, field, database):
        ##  Tenta coletar o valor de algum campo pelo user id.
        #
        # Caso seja encontrado valores múltiplos é mostrado na tela
        #   os valores encontrados.
        # Caso algum dado nao exista no banco de dados 
        #   entao a variável de retorno recebe um valor nulo.
        try:
            ret = database.objects.get(identity=uid, field=field)
            ret = ret.value

        except database.MultipleObjectsReturned:
            ret = map(lambda x: x.value, database.objects.filter(
                    identity=uid, field=field))

        except database.DoesNotExist:
            ret = None 

        return ret

    def __change_field_value(self, uid, field, value, database):
        ##  Tenta coletar o valor de algum campo pelo user id.
        #
        # Caso seja encontrado valores múltiplos é mostrado na tela
        #   os valores encontrados.
        # Caso algum dado nao exista no banco de dados 
        #   entao a variável de retorno recebe um valor nulo.
        try:
            ret = database.objects.get(identity=uid, field=field)
            ret.value = value

        except database.DoesNotExist:
            data = database(identity=uid, field=field, 
                                value=value)

            data.save()

        except ( database.DoesNotExist, 
                 database.MultipleObjectsReturned ) as exc:
            raise ValueError(exc)

        else:
            ret.save()

    def dataIn(self, dict_field_value, database):
        # Coleta identidades ordenadas do modelo requisitado.
        catch = Identities.objects.filter(
            model=database.__name__).order_by('identity')

        if not catch:
            # Tenta coletar o último id inserido.
            #   Caso não tenha ocorrido nenhum registro de contas então
            #   é atribuído o valor inicial como '1'
            try:
                # Coleta o ultimo ID inserido no identity do database.
                lastid = database.objects.order_by('-identity')[0]
                # Newid será a identity do novo usuário.
                newid = lastid.identity + 1
            except IndexError:
                newid = 1
        else:
            # Atribui o menor valor de identidade à nova conta a ser criada 
            #   e retira este número do banco de dados de id's disponíveis.
            newid = catch[0].identity
            catch[0].delete()
        
        # Percorre o dicionário ligado aos campos a seu valores.
        for fields in dict_field_value:
            # Insere novos dados: identidade, campo e a novo valor.
            data = database(identity=newid, field=fields,
                             value=dict_field_value[fields])
            # Salva os novos dados no database.
            data.save()

    def fetchDelUser(self, username, database):
        # Tenta procurar se o username existe no banco de dados.
        # Caso não exista, é emitido um erro.
        try:
            # Filtra o database pelo nome do usuario.
            uid = database.objects.get(field='NAME',value=username)
            # Coleta a ID do usuário
            uid = uid.identity

        # Caso usuário não exista, então é retornado para o Business
        # que não foi encontrado.
        except (database.DoesNotExist, database.MultipleObjectsReturned) as exc: 
            raise ValueError(exc)
                
        # Tenta filtrar os dados de um ID.
        # Caso não exista, é emitido um erro.
        try:   
            # Lista da filtragem dos dados de um determinado ID.
            accdel = database.objects.filter(identity=uid)
            # Lista dos dados é deletada do database.
            accdel.delete()
       
        except (database.DoesNotExist, 
            database.MultipleObjectsReturned) as exc: 
            raise ValueError(exc)
        else:
            # Salva o Id deletado na model de Id's disponíveis.
            newid = Identities(identity=uid, model=database.__name__)
            newid.save()

            return True

    def fetchDelCour(self, courMatric, database):
        # Tenta procurar se o username existe no banco de dados.
        # Caso não exista, é emitido um erro.
        try:
            # Filtra o database pelo nome do usuario.
            uid = database.objects.get(field='MATRIC',value=courMatric)
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
        else:  
            # Salva o Id deletado na model de Id's disponíveis.
            newid = Identities(identity=uid, model=database.__name__)
            newid.save()

            return True

    def fetchUser(self, username, database):
        acc = []

        try:
            uid = database.objects.get(field='NAME',value=username)
            uid = uid.identity

            sf = lambda x: self.__select_field(uid, x, database)

            fetchdict = {
                    'NAME' :        sf('NAME'),
                    'PASSWORD' :    sf('PASSWORD'),
                    'COURSES' :     sf('COURSE'),
                    'AVATAR' :      sf('AVATAR'),
                    'EMAIL' :       sf('EMAIL'),
                    'MATRIC' :      sf('MATRIC'),
                    'BIOS' :        sf('BIOS'),
                    'CAMPUS' :      sf('CAMPUS'),
                    'SEX' :         sf('SEX'),
            }

            if database is Student:
                fetchdict['GRADES'] = sf('GRADE')
                fetchdict['INTERESTS'] = sf('INTEREST')
                fetchdict['LANGUAGE'] = sf('LANGUAGE')

            acc.append(fetchdict)

        except database.DoesNotExist as exc:
            acc = []
        except database.MultipleObjectsReturned as exc:
            raise ValueError(exc)

        return acc

    def fetchCour(self, courMatric, database):
        acc = []

        ## Tenta coletar a identidade do curso pela matrícula.
        #
        #   Caso curso não exista então lista de retorno é retornada sem
        #		nenhum valor.
        try:
            uid = database.objects.get(field='MATRIC',value=courMatric)
            uid = uid.identity

            sf = lambda x: self.__select_field(uid, x, database)

            # Coleta os valores dos campos de Professor responsável pelo curso
            # e o nome determinado à ele.
            fetchdict = {
                'COURMATRIC' :  sf('MATRIC'),
                'PROFESSOR' :   sf('PROFESSOR'),
                'NAME' :        sf('NAME'),
                'STUDENTS' :    sf('STUDENTS'),
        	}

            acc.append(fetchdict)

        except database.DoesNotExist:
            acc = []
        except database.MultipleObjectsReturned as exc:
            raise ValueError(exc)

        return acc

    def fetchAllUser(self, database):
        al = []

        try:
            lastid = database.objects.order_by('-identity')[0]

            for uid in range(1,lastid.identity+1):
                sf = lambda x: self.__select_field(uid, x, database)

                fetchdict = {
                        'NAME':     sf('NAME'),
                        'MATRIC':   sf('MATRIC'),
                        'EMAIL':    sf('EMAIL'),
                }

                al.append(fetchdict)

        except database.DoesNotExist and IndexError:
            al = []
        except database.MultipleObjectsReturned as exc:
            raise ValueError(exc)

        return al

    def fetchAllCour(self, database):
        al = []

        try:
            lastid = database.objects.order_by('-identity')[0]

            for uid in range(1,lastid.identity+1):
                sf = lambda x: self.__select_field(uid, x, database)

                fetchdict = {
                        'NAME':         sf('NAME'),
                        'COURMATRIC':   sf('MATRIC'),
                        'PROFESSOR':    sf('PROFESSOR'),
                }

                al.append(fetchdict)

        except database.DoesNotExist and IndexError:
            al = []
        except database.MultipleObjectsReturned as exc:
            raise ValueError(exc)

        return al

    def editUser(self, request, database):
        # Tenta procurar se o username existe no banco de dados.
        # Caso não exista, é emitido um erro.
        try:
            # Filtra o database pelo nome do usuario.
            uid = database.objects.get(field='NAME',value=request['username'])
            # Coleta a ID do usuário
            uid = uid.identity

        # Caso usuário não exista, então é retornado para o Business
        # que não foi encontrado.
        except (database.DoesNotExist, database.MultipleObjectsReturned) as exc: 
            raise ValueError(exc)
                
        # Tenta filtrar os dados de um ID.
        # Caso não exista, é emitido um erro.
        try:   
            sf = lambda x, y: self.__change_field_value(uid, x, y, database)

            sf('EMAIL', request['userEmail'])

            if database != Adm:
                sf('MATRIC', request['userMatric'])
                sf('CAMPUS', request['userCampus'])
                sf('SEX', request['userSex'])
       
        except (database.DoesNotExist, 
            database.MultipleObjectsReturned) as exc: 
            raise ValueError(exc)

    def editCour(self, request, database):
        # Tenta procurar se o username existe no banco de dados.
        # Caso não exista, é emitido um erro.
        try:
            # Filtra o database pelo nome do usuario.
            uid = database.objects.get(field='MATRIC',value=request['courMatric'])
            # Coleta a ID do usuário
            uid = uid.identity

        # Caso usuário não exista, então é retornado para o Business
        # que não foi encontrado.
        except (database.DoesNotExist, database.MultipleObjectsReturned) as exc: 
            raise ValueError(exc)
                
        # Tenta filtrar os dados de um ID.
        # Caso não exista, é emitido um erro.
        try:   
            sf = lambda x, y: self.__change_field_value(uid, x, y, database)

            sf('MATRIC', request['courMatric'])
            sf('PROFESSOR', request['courProfessor'])
            sf('NAME', request['courName'])
       
        except (database.DoesNotExist, 
            database.MultipleObjectsReturned) as exc: 
            raise ValueError(exc)

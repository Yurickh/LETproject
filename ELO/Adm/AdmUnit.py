#coding: utf-8

## TODO:
#   233: verificar validade do request.POST, tal qual if anterior.
#   Colocar permissões de Adm e God diferenciadas.
#   Implementar deleção de contas.
#   Implementar confirmação de senha do Adm após qualquer ação realizada.
#   Implementar log de eventos que o Adm ou God realizar.
#   Verificar melhorias na conferência de ação em request.POST em UIAdm

## @file AdmUnit.py
#   Este arquivo é responsável pelo armazenamento de todas as camadas 
#   correspondentes ao módulo de administrador. 
#   Os métodos aqui são criados e chamados pela Factory (MainUnit.py)
#   quando necessários. 
#   São responsáveis por cadastrar, deletar e editar alunos e professores 
#   no banco de dados, criar cursos e ver um log sobre os últimos eventos no
#   sistema.

from abc import *

import ELO.index as lang

from ELO.models import Adm, Student, Professor, Courses, God

from forms import (
    RegUserForm,
    SrcUserForm,
    ConfAdmForm,
    RegCourForm,
    SrcCourForm)

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

    ## Cria uma conta no database.
    #   Podendo ser esta uma conta de Estudante, Professor ou um Curso.
    #   
    #   @arg    form    Valores dos campos para registro validados.
    #
    @abstractmethod
    def regAccount(self, request, form): pass
   
    ## Edita dados de um conta no database.
    #   Podendo ser estes de uma conta de Estudante, Professor ou um Curso.  
    #
    #   @arg    form    Valores dos campos para edição validados.
    #
    @abstractmethod
    def attAccount(self, request): pass

    ## Deleta uma conta no database.
    #   Podendo ser esta uma conta de Estudante, Professor ou um Curso.
    @abstractmethod
    def delAccount(self, request): pass

    ## Procura conta do database.
    #   Podendo ser esta uma conta de Estudante, Professor ou um Curso.
    #
    #   @return data    Dados da conta procurada.
    @abstractmethod
    def fetchAccount(self, request): pass

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

    ## Insere Estudantes ou Professores em algum Curso.
    #
    #   @arg    course_id   Matrícula do Curso que irá receber as inserções.
    #
    #   @arg    user_id     Matrícula do Usuário que será inserido.
    #
    #   @arg    model       Modelo do usuário que será inserido no Curso.
    @abstractmethod
    def insert_User(self, course_id, user_id, model): pass

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

## Camada de interface do Administrador para o módulo de Administração.
#   Deve carregar o devido template, contendo campos onde será
#   permitido a criação, edição e deleção de contas do tipo Estudante,
#   Professor e Cursos.
#   Caso seja feito o pedido de alteração em qualquer condição
#   citada acima então será chamada uma caixa com formulários
#   requisitando os devidos dados necessários de cada ação.
class UiAdm(IfUiAdm): 

    def run(self, request, action=None, model=None):
        print request.POST
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
        if request.method == "POST":
            ## @if Confere se é uma ação de registro pedido pelo Adm.
            #
            #   Caso seja então é feito a verificação do modelo de conta
            #   para que a validação do form seja conforme o requisitado.
            #
            #   Caso contrário confere se é uma ação do tipo atualização ou
            #   deleção, onde, ambas enviam um POST de procura de usuário
            #   e esperam algum retorno das informações deste.
            if "reg" in request.POST:
                try:
                    ## @if Confere se o modelo de Conta é do tipo Estudante
                    #       ou Professor.
                    #
                    #   Caso seja então é coletado o formulário da requisição
                    #   para a validação deste.
                    #
                    #   Caso contrário confere se o modelo da conta é do tipo
                    #   Curso, e faz a mesmas validações para o formulário
                    #   adequado para Cursos.
                    #
                    #   Por último caso, caso não seja nenhum destes 3 modelos
                    #   iŕa ser criada uma excessão de erro indicando Modelo
                    #   inválido.
                    if request.POST['model'] == 'Student' or \
                        request.POST['model'] == 'Professor':
                        # Coleta os forms de registro de estudante ou professor 
                        # a partir da requisição POST.
                        form = RegUserForm(request.POST)
                    elif request.POST['model'] == 'Course':
                        # Coleta os forms de registro de Cursos a partir da 
                        # requisição POST.
                        form = RegCourForm(request.POST)
                    else:
                        # TODO ERRO PARA MODELO INCORRETO.
                        raise ValueError(lang.DICT['EXCEPTION_404_ERR'])

                    ## @if Confere se form de registro é valido.
                    #
                    #   Se form for adequado então é chamado o método 
                    #   de registro de contas que irá comunicar-se 
                    #   com o banco de dados depois da validação das 
                    #   informações passadas pelo request.POST.
                    #
                    #   Caso contrário, é lançada exceção de erro referente à
                    #   form inválido.
                    if form.is_valid():
                        self.bus.regAccount(request, form)

                # Se houver qualquer problema referente as passagens dos forms 
                # e conferência da validação dos mesmos então o 
                # administrador será passado para a página inicial.
                except ValueError as exc:
                    return render(request, "Adm/home.html")


            elif action == "insert":
                # Dicionário com informações do curso procurado pelo Adm.
                dCourse = {}

                try:
                    # Coleta os forms de busca a partir da requisição POST.
                    form = SrcCourForm(request.POST)

                    ## @if Confere se form de busca é valido.
                    #
                    #   Se form for adequado então é chamado o método 
                    #   de procura de contas que irá comunicar-se 
                    #   com o banco de dados depois da validação das 
                    #   informações passadas pelo request.POST.
                    #
                    #   Caso contrário, é lançada exceção de erro referente à
                    #   form inválido.
                    if form.is_valid():
                        dCourse = self.bus.fetchAccount(request)

                        ## @if Confere se dicionário de informações do Curso
                        #       ainda continua nulo.
                        #
                        #   Caso esteja nulo então é lançado excessão de conta
                        #   inexistente.
                        if not dCourse:
                            raise ValueError(lang.DICT['EXCEPTION_INV_USR_NM'])

                        # Força a ter uma estruturação correta de dicionário.
                        dCourse = dict(dCourse)

                        # Renderiza uma página assíncrona de informação da
                        # conta requisitada.
                        return render(request, 
                                      "Adm/edit_course.html", {'data':dCourse})
                    else:
                        raise ValueError(lang.DICT['EXCEPTION_INV_FRM'])

                # Se houver qualquer problema referente as passagens dos forms 
                # e conferência da validação dos mesmos então o 
                # administrador será passado para a página inicial.
                except ValueError:
                    return HttpResponseRedirect('/')

            elif request.POST['action'] == 'att' or \
                    request.POST['action'] == 'scrdel':
                # Dicionario com informações do usuário procurado pelo Adm.
                dUser = {}
                
                action = request.POST['action']
                model = request.POST['model']

                try:
                    if model == "Course":
                        # Coleta os forms de busca a partir da requisição POST.
                        form = SrcCourForm(request.POST)
                    else:
                        form = SrcUserForm(request.POST)

                    ## @if Confere se form de busca é valido.
                    #
                    #   Se form for adequado então é chamado o método 
                    #   de procura de contas que irá comunicar-se 
                    #   com o banco de dados depois da validação das 
                    #   informações passadas pelo request.POST.
                    #
                    #   Caso contrário, é lançada exceção de erro referente à
                    #   form inválido.
                    if form.is_valid():
                        dUser = self.bus.fetchAccount(request)

                        ## @if Confere se dicionário de informações de usuário
                        #       ainda continua nulo.
                        #
                        #   Caso esteja nulo então é lançado excessão de conta
                        #   inexistente.
                        if not dUser:
                            raise ValueError(lang.DICT['EXCEPTION_INV_USR_NM'])

                        # Força a ter uma estruturação correta de dicionário.
                        dUser = dict(dUser)

                        # Renderiza uma página assíncrona de informação da
                        # conta requisitada.
                        return render(request, 
                                      "Adm/info.html", {'data':dUser, 
                                                        'action': action,
                                                        'model' : model, 
                                                        })
                    else:
                        raise ValueError(lang.DICT['EXCEPTION_INV_FRM'])

                # Se houver qualquer problema referente as passagens dos forms 
                # e conferência da validação dos mesmos então o 
                # administrador será passado para a página inicial.
                except ValueError:
                    return HttpResponseRedirect('/')

            # Após a coleta da requisição o administrador será retornado à 
            # página inicial de controle.
            return HttpResponseRedirect('/')
                                         
        else:
            if not (action or model):
                return render(request, "Adm/home.html")
            else:
                ## @if Confere qual a ação requisitada.
                #
                #   Caso for uma ação de registro então é passado os forms de
                #   registro de acordo com o modelo de conta requisitado.
                #
                #   Caso for uma ação de atualização, deleção ou inserção de 
                #   usuário em algum Curso é passado o form de busca de conta.
                #
                #   Caso contrário, é passado para a página renderizada erro
                #   de formulário.   
                if action == "reg":
                    if model == "Student" or model == "Professor":
                        form = RegUserForm()
                    elif model == "Course":
                        form = RegCourForm()
                    else:   
                        # TODO ERRO PARA MODELO INCORRETO.
                        raise ValueError(lang.DICT['EXCEPTION_404_ERR'])
                elif action == "att" or action == "srcdel":
                    if model == "Student" or model == "Professor":
                        form = SrcUserForm()
                        print form
                    elif model == "Course":
                        form = SrcCourForm()
                    else:
                        # TODO ERRO PARA MODELO INCORRETO.
                        raise ValueError(lang.DICT['EXCEPTION_404_ERR'])
                elif action == "del":
                    possible = self.bus.delAccount(request)
                    print possible
                elif action == "insert":
                    form = SrcCourForm()
                else:
                    form = lang.DICT["ERROR_FORM"]
                return render(request, "Adm/edit.html", {'form': form,
                                                         'action' : action,
                                                         'model' : model,
                                                        })


## Camada de negócio para o módulo de administração.
#   Deve ser capaz de manipular os dados do sistema,
#   dando as devidas diretrizes ao banco de dados para que seja
#   inserido, atualizado ou deletado dados sobre uma determinada
#   conta, podendo ser esta de um Estudante, Professor ou de um Curso.
class BusAdm(IfBusAdm): 

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
        try:
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
                    dict_data[newField] = form.cleaned_data[
                                                field].value
            ## Verifica qual e o tipo do modelo requisitado para inserção 
            #   de nova conta.
            #    
            #   Caso a requisição venha com outro modelo não especificado nos
            #   condicionais então é emitido erro.
            try:
                db = None

                model = str(request.POST['model'])

                if model == "Student":
                    db = Student
                elif model == "Professor":
                    db = Professor
                elif model == "Course":
                    db = Courses 
                else:
                    raise ValueError(lang.DICT['EXCEPTION_404_ERR'])

            except ValueError as exc:
                raise ValueError(lang.DICT['EXCEPTION_404_ERR'])

            ## @if Verifica se a requisição pede outro modelo diferente de 
            #       Curso.
            #       
            #   Caso não for do modelo de Curso então é adionado a linguagem
            #   com valor default de Português.
            if model != "Course":
                # Escolhe uma linguagem padrão para cadastro do usuário 
                # recente.
                dict_data['LANGUAGE'] = 'pt-br'

            # É passado o dicionário de campos e valores do novo registro, e
            # o modelo de conta requisitado para criação destas informações 
            # no banco de dados (Persistência).
            self.pers.data_in(dict_data, db)

        except ValueError as exc:
            raise ValueError(lang.DICT['EXCEPTION_INV_FRM'])

        
    def attAccount(self, request): pass
        
    def delAccount(self, request):
        try:
            db = None

            model = str(request.POST['model'])

            if model == "Student":
                db = Student
            elif model == "Professor":
                db = Professor
            elif model == "Course":
                db = Courses 
            else:
                raise ValueError(lang.DICT['EXCEPTION_404_ERR'])

        except ValueError as exc:
            raise ValueError(lang.DICT['EXCEPTION_404_ERR'])

        data = self.pers.fetch_del(request.POST['username'], db)

        return data

    def fetchAccount(self, request):
        try:
            # Inicializa modelo como nulo.
            db = None

            # Força modelo da conta passado pela requisição a ser uma String.
            model = str(request.POST['model'])

            ## @if Confere qual o modelo da conta procurado.
            #
            #   Caso seja Estudante este é alocado em uma variável temporária.
            #
            #   Caso seja Professor este é alocado em uma variável temporária.
            #
            #   Caso seja Curso este é alocado em uma variável temporária.   
            #   
            #   Caso contrário, irá emitir excessão de modelo inválido.
            if model == "Student":
                db = Student
            elif model == "Professor":
                db = Professor
            elif model == "Course":
                db = Courses 
            else:
                # TODO ERRO PARA MODELO INCORRETO.
                raise ValueError(lang.DICT['EXCEPTION_404_ERR'])

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

            return data
        except ValueError as exc:
            raise ValueError(lang.DICT['EXCEPTION_404_ERR'])


    ## Edita campos de um usuario.
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

class PersAdm(IfPersAdm):

    def data_in(self, dict_field_value, database):
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
        
        # Percorre o dicionário ligado aos campos a seu valores.
        for fields in dict_field_value:
            # Insere novos dados: identidade, campo e a novo valor.
            data = database(identity=newid, field=fields,
                             value=dict_field_value[fields])
            # Salva os novos dados no database.
            data.save()

    def insert_User(self, course_id , user_id, model):
        ##  Tenta coletar a identidade do Curso pela matrícula.
        #
        # Caso não exista ou seja encontrado valores múltiplos, 
        #   é emitido erro.
        try:
            # Filtra o database pela matrícula do Curso.
            uid = Courses.objects.get(field='MATRIC',value=course_id)
            # Coleta a ID do Curso encontrado.
            uid = uid.identity

            ## Tenta coletar a lista de Estudantes ou Professores de algum 
            #   Curso.
            #
            # Caso seja encontrado valores múltiplos então é emitido erro.
            #
            # Caso lista de Estudantes ou Professores não exista então
            # novo valor é iniciado como primeiro item da lista.
            try:
                # Coleta a partir do ID do curso a lista de Estudantes ou 
                # Professores existentes no Curso.
                data = Courses.objects.get(identity=uid, field=model.upper())
                # Transforma lista unicode para formato de lista padrão.
                new_data = eval(data.value)
                # Adiciona ao final da lista um novo valor de Estudante ou
                # Professor.
                new_data.append(user_id)
                # Retorna lista com novo valor à lista do Curso direcionado.
                data.value = new_data

            except ( Courses.MultipleObjectsReturned ) as exc:
                raise ValueError(exc)

            except ( Courses.DoesNotExist ) as exc:
                new_list = []
                new_list.append(user_id)
                data = Courses(identity=uid, field=model.upper(), 
                                value=new_list)
            # Salva os novos dados no database. 
            data.save()

        except ( Courses.DoesNotExist, 
                 Courses.MultipleObjectsReturned ) as exc:
            raise ValueError(exc)



    def update(self, username, field, newdata, database): 
        ##  Tenta coletar a identidade da conta pelo nome determinado a ela.
        #
        # Caso não exista ou seja encontrado valores múltiplos , é
        #   emitido erro.
        try:
            # Filtra o database pelo nome do usuario.
            uid = database.objects.get(field='NAME', value=username)
            # Coleta a ID do usuário encontrado.
            uid = uid.identity
                
            try:
                # Coleta a partir do ID do curso a lista do campo
                # que deseja atualizar.
                data = database.objects.get(identity=uid, field=field.upper())
                # Nova informação é colocada no tipo que deseja atualizar.
                data.value = newdata
            # Caso o novo valor a ser colocado já exista então este 
            # continua o mesmo.
            except database.DoesNotExist:
                data = database(identity=uid, field=field.upper(), 
                                value=newdata)
            # Salva os novos dados no database.
            data.save()

        except ( database.DoesNotExist, 
                 database.MultipleObjectsReturned ) as exc:
            raise ValueError(exc)

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

            return True
       
        except ( database.DoesNotExist, 
                database.MultipleObjectsReturned ) as exc:
            raise ValueError(exc)

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

    def fetchUser(self, username, database):

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

    def fetchCour(self, courMatric, database):
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
            fetchset = [
                ('professor',   sf('PROFESSOR')),
                ('name',        sf('NAME')),
                ('students',     sf('STUDENTS')),
        	]

        except database.DoesNotExist as exc:
            fetchset = []

        return fetchset



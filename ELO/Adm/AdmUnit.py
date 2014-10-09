#coding: utf-8

## TODO:
#   Passar para inglês os termos internos ao sistema que estão em português. 
#       (e.g. 214, 234, 240)
#   Ajeitar os nomes das forms. (Adm/forms)
#   Atentar ao padrão de 80 caracteres/linha.
#   233: verificar validade do request.POST, tal qual if anterior.

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

from ELO.models import Adm, Student, Professor
from forms import (
    AdmRegStu_ProfForm,
    AdmDelStu_ProfForm,
    confAdm,
    AdmRegCourForm,
    AdmSrcCourForm,
    AdmDelCourForm)

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

    ## Edita dados de um conta no database.
    #   Podendo ser este de uma conta de Estudante, Professor ou um Curso.
    #
    #   @arg field      Nome do objeto a ser registrado.
    #
    #   @arg form       Objeto form que contém os dados.
    @abstractmethod
    def editAccounts(self, dict_field_value, action, database, form): pass

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
        ## @if Verifica qual o propósito do submit.
        #   Caso seja POST, a requisição ocorre após a submissão de uma form,
        #       podendo ser ela de registro, edição ou deleção.
        #   Caso não seja e não ocorra a passagem dos campos de ação e modelo,
        #       a requisição há de ser um GET, para mostrar a página principal
        #       de Adm.
        #   Em último caso será a requisição do Javascript, denominada como 
        #       AJAX, que irá solicitar em tempo de evento dos dialogs 
        #       iniciados.
        #   Será passada informações para requisitar os forms adequados e 
        #       informações do usuário procurado para uma possível edição ou 
        #       deleção.
        if request.method == "POST":

            #--------------------------sugestões do tio Yurick
            # sugestão de como fazer essa verificação, mas pode fazer do jeito
            # que preferir

            if 'type' in request.POST and request.POST['type'] == 'info':
                try:
                    # pus aqui só para não precisar mudar a assinatura da
                    # editAccounts, já que 'action' é um campo redudante
                    action = "atualizar"

                    form = AdmDelStu_ProfForm(request.POST)
                    if form.is_valid():
                        # aconselho usar um método diferente
                        # para recuperação de dados, bem como corrigir
                        # os argumentos redundantes
                        d_user = self.bus.editAccounts(request.POST,
                                                        action,
                                                        Student,
                                                        form)
                        if not d_user:
                            raise ValueError("TALVEZ ALGUMA MENSAGEM DE ERRO?")

                        d_user = dict(d_user)

                        return render(request, 
                                      "Adm/info.html", 
                                      {'data':d_user})
                    else:
                        raise ValueError(lang.DICT['EXCEPTION_INV_FRM'])
                except ValueError as exc:
                    # falta criar algum suporte para mensagem de erro
                    return HttpResponseRedirect('/')

            #-------------------------

            if "registrar" in request.POST:
                try:
                    # Coleta os forms adequados a partir da requisição POST.
                    form = AdmRegStu_ProfForm(request.POST)

                    # Se form for adequado então é chamado o método de edição 
                    #   de contas que irá comunicar-se com o banco de dados 
                    #   depois de uma validação das informações passadas pelo
                    #   request.POST.
                    if form.is_valid():
<<<<<<< HEAD
                        self.bus.editAccounts(request.POST, action, Student, form) # model entra aqui no lugar de student
                    # Caso contrário irá surgir um erro de que há dados incorretos.
=======
                        self.bus.editAccounts(request.POST,action, Student, form)
                    # Caso contrário irá surgir um erro de que há dados
                    #   incorretos.
>>>>>>> 198179b0ebd94d135f569e5a8565f286444d3203
                    else:
                        raise ValueError(lang.DICT['EXCEPTION_INV_FRM'])
                # Se houver qualquer problema referente as passagens dos forms 
                #   e conferência da validação dos mesmos então o 
                #   administrador será passado para a página inicial.
                except ValueError as exc:
                    return render(request, "Adm/home.html")
            elif "atualizar" in request.POST:
                d_user = self.bus.editAccounts(request.POST, "atualizar", Student, form = None)
                data = dict(d_user)

                return render(request, "Adm/info.html", {'data' : data})
            
            elif "apagar" in request.POST:
                d_user = self.bus.editAccounts(request.POST, "apagar", Student, form = None)
                data = dict(d_user)

                return render(request, "Adm/info.html", {'data' : data})

            elif "name" in request.POST:
                form = NameForm(request.POST)
                field = "name"
            elif  "password" in request.POST:
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
                #raise ValueError(lang.DICT['EXCEPTION_INV_FRM'])
                return HttpResponseRedirect('/')
            if form.is_valid():
                self.bus.editAccounts(request.POST, field, Student, form)
                request.session.modified = True                

            # Após a coleta da requisição o administrador será retornado à página inicial de controle.
            return HttpResponseRedirect('/')

        # Quando a requisição for de GET então é retornado para a página principal.                                           
        else:
            # Chamada normal de GET.
            if not (action or model):
                return render(request, "Adm/home.html")
            # Caso contrário, no caso de requisições do tipo AJAX, 
            #   irá ser repassado forms adequados ao pedido ou será feito
            #   buscas de dados do usuário requisitado.
            else:
                if action == "reg":
                    form = AdmRegStu_ProfForm()
                elif action == "att" or action == "del":
                    form = AdmDelStu_ProfForm()
                else:
                    form = lang.DICT["ERROR_FORM"]
                return render(request, "Adm/edit.html", {'form': form,
                                                         'action' : action,
                                                        })




## Camada de negócio para o módulo de administração.
#   Deve ser capaz de manipular os dados do sistema,
#   dando as devidas diretrizes ao banco de dados para que seja
#   inserido, atualizado ou deletado dados sobre uma determinada
#   conta, podendo ser esta de um Estudante, Professor ou de um Curso.
class BusAdm(IfBusAdm): 

    ## Edita dados de um conta no database.
    #   Podendo ser este de uma conta de Estudante, Professor ou um Curso.
    def editAccounts(self, dict_field_value, action, database, form):
        
        # Inicia o dicionário dict_data.
        #   Será utilizado para informar os campos e dados para registro do usuário.
        dict_data = {}
        database_fields = ['NAME', 'SEX', 'PASSWORD', 'MATRIC', 'CAMPUS','EMAIL']

        # Se for uma ação de registro do usuário.
        if action == "registrar": 
            # Percorre os campos e valores coletador no request.POST.
            for field, value in dict_field_value.items():
                # Transforma os unicodes do dicionário em strings.
                field = str(field)
                # Coleta a palavra chave do campo designado.
                #   Esta é coletada a partir dos campos contidos no dicionário.
                newField = field[4:].upper()

                # Se o campo encontrado pertence à lista de campos do database que deveriam
                # pertencer a um usuário, então este é adicionado ao dicionário que será
                # repassado para inserção no banco de dados posteriormente.
                if newField in database_fields:
                    dict_data[newField] = form.cleaned_data[field].value

            # Escolhe uma linguagem padrão para cadastro de um usuário qualquer.
            dict_data['LANGUAGE'] = 'en'

            # Se for uma entidade estudante então é feito o pedido de inserção 
            # no banco de dados com o determinado modelo.
            if database.__name__ == "Student":
                self.pers.data_in(dict_data, database)

        elif action == "atualizar":
            data = self.pers.fetch(dict_field_value['username'], Student)

            return data

        elif action == "apagar":
            data = self.pers.fetch(dict_field_value['username'], Student)

            return data

        elif action == "name":
            fpw = form.cleaned_data['password'].value
            if fpw != user['password']:
                raise ValueError(lang.DICT['EXCEPTION_INV_PW_F'])
            newdata = form.cleaned_data['newdata'].value
        elif action == "password":
            npw = form.cleaned_data['newdata'].value
            rpw = form.cleaned_data['rp_newdata'].value
            opw = form.cleaned_data['old_password'].value
            if npw != rpw:
                raise ValueError(lang.DICT['EXCEPTION_INV_PW_R'])
            if opw != user['password']:
                raise ValueError(lang.DICt['EXCEPTION_INV_PW_F'])
            newdata = npw
        elif action == "language":
            newdata = form.cleaned_data['newdata']
        elif action == "avatar":
            addr = settings.MEDIA_ROOT + u"/" + user['avatar']
            with open(addr, "wb") as destination:
                    for chunk in request.FILES['newdata'].chunks():
                        destination.write(chunk)
        else:
            newdata = form.cleaned_data['newdata'].value

        try:
            self.pers.update(user['name'], field, newdata, Student)
        except ValueError as exc:
            raise ValueError(lang.DICT['EXCEPTION_ERR_DB_U'])


## Camada de persistência para o módulo de administração.
#   Insere, atualiza ou deleta dados do banco de dados referentes aos 
#   alunos professores e cursos.
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
            data = database(identity=newid, field=fields,
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

    ##  Função que recupera todos os dados do usuário.
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



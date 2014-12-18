#coding: utf-8

## @file BaseUnit.py
#  Implementa os tipos básicos do programa.
#
#   Os tipos básicos são os blocos formadores do programa. Eles contêm
#   informações atômicas como Nome, Senha ou Matrícula, e devem ser capazes
#   de validá-los no momento de sua criação. Ou seja, caso o valor fornecido
#   não esteja de acordo com as especificações, o tipo básico não é criado
#   e lança uma exceção do tipo ValueError.

from abc import *
import hashlib

import ELO.locale.index as lang

## Interface para todos os tipos básicos.
#
#   Classe abstrata que contém os métodos get, set e del de todos os tipos
#   básicos. Estes métodos são chamados implicitamente através dos processos
#   de requisição de valor, atribuição de valor, e deleção do objeto,
#   respectivamente.
#
#   Possui um único método abstrato, o validador do tipo básico, que varia
#   de tipo para tipo, e deve ser obrigatoriamente implementado, sob a pena
#   do tipo básico não poder ser instanciado.
class IfBaseType:

    ## Especifica que IfBaseType é uma classe base abstrata (abc). 
    #   Isso significa que uma classe derivada pode ser instanciada se
    #   - e somente se - ela der "override" em todos os métodos e
    #   propriedades abstratas.
    __metaclass__ = ABCMeta

    ## Método que retorna o valor contido no tipo básico.
    #   Método GET.
    @property
    def value(self):
        return self._value

    ## Método que fixa e valida o conteúdo do tipo básico.
    #   Método SET.
    #
    #   @arg aux Recebe o valor que será validado.
    @value.setter
    def value(self, aux):
        self._validate(aux)
        self._value = aux

    ## Método que deleta o conteúdo do tipo básico.
    #   Método DEL.
    @value.deleter
    def value(self):
        del self._value

    ## Define que toda classe derivada terá um método _validate.
    @abstractmethod
    def _validate(self, value): pass

    ## Método que compara o conteúdo de dois tipos básicos.
    #   Será chamado toda vez que dois tipos básicos forem
    #   comparados através dos operadores >, <, >=, <=, == ou !=.
    #
    #   @return Retornos predefinidos do próprio python.
    def __cmp__(self, other):
        if other.value == self.value:
            return 0
        elif other.value > self.value:
            return 1
        else:
            return -1

## Classe container de senhas.
#   Deve ser responsável não somente por armazenar, mas também por
#   encriptar a string recebida.
class Password(IfBaseType):
    _value = None

    ## Construtor da classe.
    #   Valida e encripta a string recebida.
    #
    #   @arg        value       String a ser armazenada.
    #
    #   @exception  ValueError  Exceção lançada no caso do
    #                           valor de entrada não passar pelos
    #                           critérios do método _validate().
    def __init__(self, value):
        try:
            self._validate(value)
        except ValueError as exc:
            del self
            raise exc
        self._value = hashlib.sha256(value).hexdigest()
        self._value = hashlib.md5(self._value).hexdigest()

    ## Validator da classe.
    #   Verifica se o tamanho da string recebida (value) está correta.
    #
    #   @arg        value       String a ser validada.
    #
    #   @exception  ValueError  Lançada no caso do tamanho de
    #                           value ser menor do que 6
    #                           caracteres.
    def _validate(self, value):
        if(len(value) < 6):
            raise ValueError(lang.DICT['EXCEPTION_INV_PW_S'])

    @property
    def value(self):
        return self._value

    ## Método setter específico de password.
    #   Sobrescreve o setter definido na interface para que ocorra
    #   a encriptação de forma correta.
    #
    #   @arg value String a ser validada e encriptada.
    @value.setter
    def value(self, value):
        self._validate(value)
        self._value = hashlib.sha256(value).hexdigest()
        self._value = hashlib.md5(self._value).hexdigest()

## Classe container de nomes.
#   Responsável por armazenar uma string que servirá para identificação
#   dos usuários do sistema.
class Name(IfBaseType):

    _value = None

    ## Construtor da classe.
    #   Responsável por impedir a criação do tipo básico em caso de
    #   falha.
    #
    #   @arg value String a ser armazenada.
    def __init__(self, value):
        try:
            self._validate(value)
        except ValueError as exc:
            del self
            raise exc
        self._value = value

    ## Validator da classe.
    #   Verifica se a string de entrada (value) está de acordo com as
    #   especificações.
    #
    #   @arg       value        String a ser validada.
    #
    #   @exception ValueError   Exceção lançada no caso da string de
    #                           entrada ser vazia ou conter algum
    #                           caractere não-alfanumérico.
    def _validate(self, value):
        if len(value) > 32:
            raise ValueError(lang.DICT['EXCEPTION_INV_NM_B'])
        else: 
            if len(value) == 0:
                raise ValueError(lang.DICT['EXCEPTION_INV_NM_S'])
            else:
                temp = unicode.isalnum(value.replace(" ", ""))
                if temp == False:
                    raise ValueError(lang.DICT['EXCEPTION_INV_NM_F'])

## Classe container de matrículas.
#   Responsável por armazenar um número inteiro que identifica
#   univocamente alguns usuários do sistema.
class Matric(IfBaseType):

    _value = None

    ## Construtor da classe.
    #   Responsável por impedir a criação de um tipo básico com
    #   valor inválido.
    #
    #   @arg value Número inteiro a ser armazenado no tipo básico.
    def __init__(self, value):
        try:
            self._validate(value)
        except ValueError as exc:
            del self
            raise exc
        self._value = value

    ## Validator da classe.
    #   Responsável por garantir a coerência da matrícula armazenada
    #   com as especificações do sistema.
    #
    #   @arg       value    Inteiro a ser validado.
    #
    #   @exception ValueError   Exceção lançada no caso de value
    #                           exceder a faixa dinâmica permitida
    #                           para a matrícula (1-9 dígitos).
    def _validate(self, value):
        try: int(value)
        except ValueError: raise ValueError(lang.DICT['EXCEPTION_INT_MT_F'])

        if value > 999999999:
            raise ValueError(lang.DICT['EXCEPTION_INV_MT_B'])
        elif value < 1:
            raise ValueError(lang.DICT['EXCEPTION_INV_MT_S'])
        
## Classe container de texto.
#   Responsável por armazenar texto corrido, como em descrições,
#   biografias, resumos etc.
class PlainText(IfBaseType):
    _value = None

    ## Construtor da classe.
    #   Responsável por impedir a criação de um tipo básico com
    #   conteúdo inválido.
    #
    #   @arg value String a ser validada e armazenada.
    def __init__(self, value):

        try:
            self._validate(value)
        except ValueError as exc:
            del self
            raise exc
        self._value = value

    ## Validator da classe.
    #   Responsável pela devida verificação da validade de value.
    #
    #   @arg        value       String a ser validada.
    #
    #   @exception  ValueError  Exceção lançada no caso de
    #                           value exceder 1024 caracteres.
    def _validate(self, value):
        if len(value) > 1024:
            raise ValueError(lang.DICT['EXCEPTION_INV_PT_B'])

## Classe container de Campus.
#   Irá armazenar um inteiro que identifica univocamente um Campus.
#   A associação Campus-Id será tratada em uma tabela à parte.
class Campus(IfBaseType):

    _value = None

    ## Construtor da classe.
    #   Responsável por impedir a criação de um tipo básico com
    #   conteúdo inválido.
    #
    #   @arg value Inteiro a ser armazenado.
    def __init__(self, value):
        try:
            self._validate(value)
        except ValueError as exc:
            del self
            raise exc
        self._value = value

    ## Validador da classe.
    #   Capaz de identificar se o valor de entrada está dentro dos
    #   requisitos do sistema.
    #
    #   @value      value       Inteiro a ser validado.
    #
    #   @exception  ValueError  Exceção lançada no caso de
    #                           value ser negativo.
    def _validate(self, value):
        try: int(value)
        except ValueError: raise ValueError(lang.DICT['EXCEPTION_INV_CP_F'])

        if value <= 0:
            raise ValueError(lang.DICT['EXCEPTION_INV_CP_S'])

## Classe container de sexo.
#   Responsável por armazenar um caractere relativo a identificação
#   do sexo do usuário.
class Sex(IfBaseType):
    _value = None
    
    ## Construtor da classe.
    #   Capaz de impedir a criação de um tipo básico com conteúdo
    #   inválido.
    #
    #   @arg        value       Caractere a ser armazenado no
    #                           tipo básico.
    #
    #   @exception  ValueError  Exceção lançada para advertir
    #                           que value está inválido.
    def __init__(self, value):
        try:
            self._validate(value)
        except ValueError as exc:
            del self
            raise exc
        self._value = value

    ## Validador da classe.
    #   Deve ser capaz de lançar uma exceção no caso de value não ser
    #   compatível com as especificações do sistema.
    #
    #   @arg        value       Caractere a ser validado.
    #
    #   @exception  ValueError  Exceção a ser lançada no caso do
    #                           caractere validado não ser F ou M.
    def _validate(self, value):
        if value.upper() != u"M" and value.upper() != u"F":
            raise ValueError(lang.DICT['EXCEPTION_INV_SX_F'])

## Classe container de endereço do sistema.
#   Capaz de armazenar uma string que representa o endereço de um arquivo
#   na árvore de diretórios do servidor.
class Link(IfBaseType):
    _value = None

    ## Construtor da classe.
    #   Impede a criação de um tipo básico com conteúdo inválido.
    #
    #   @arg        value       String a ser armazenada.
    #
    #   @exception  ValueError  Exceção lançada no caso da
    #                           invalidez de value.
    def __init__(self, value):
        try:
            self._validate(value)
        except ValueError as exc:
            del self
            raise exc
        self._value = value

    ## Validador da classe.
    #   Verifica se a string de entrada está de acordo com as
    #   especificações do sistema.
    #
    #   @arg        value       Stringa  ser validada.
    #   
    #   @exception  ValueError  Exceção lançada no caso de
    #                           value não ser composto de
    #                           caracteres exclusivamente
    #                           alfanuméricos, com exceção
    #                           das barras do sistema.
    def _validate(self, value):
        nobar = value.replace("/", "")
        nobar = value.replace(".", "")
        if len(value) == 0:
            raise ValueError(lang.DICT['EXCEPTION_INV_LK_S'])
        elif unicode.isalnum(nobar) != False or len(nobar) == 0:
            raise ValueError(lang.DICT['EXCEPTION_INV_LK_F'])

## Classe container de notas.
#   Armazena números que representam notas dos alunos nas atividades.
class Grades(IfBaseType):
    _value = None

    ## Contrutor da classe.
    #   Deve ser capaz de abortar a criação do tipo básico no caso do
    #   valor passado ser inválido.
    #
    #   @arg        value       Inteiro a ser armazenado.
    #
    #   @exception  ValueError  Exceção lançada no caso de
    #                           value não atender as
    #                           especificações do sistema.
    def __init__(self, value):
        try:
            self._validate(value)
        except ValueError as exc:
            del self
            raise exc
        self._value = value

    ## Validator da classe.
    #   Deve verificar a validade do argumento a ele passado, lançando
    #   uma exceção em caso contrário.
    #
    #   @arg        value       Inteiro a ser validado.
    #
    #   @exception  ValueError  Exceção lançada no caso de
    #                           value ser negativo ou maior
    #                           do que 100.
    def _validate(self, value):
        try: int(value)
        except ValueError: raise ValueError(lang.DICT['EXCEPTION_INV_GR_F'])

        if value < 0:
            raise ValueError(lang.DICT['EXCEPTION_INV_GR_S'])
        elif value > 100:
            raise ValueError(lang.DICT['EXCEPTION_INV_GR_B'])

## Classe container de email.
#   Este tipo básico irá armazenar emails para contato e identificação
#   dos usuários.
class Mail(IfBaseType):
    _value = None

    ## Construtor da classe.
    #   Deve impedir a criação do tipo básico caso seu conteúdo não
    #   esteja de acordo com as especificações.
    #
    #   @arg        value       String a ser armazenada no
    #                           tipo básico.
    #
    #   @exception  ValueError  Exceção lançada no caso do
    #                           valor passado não ser válido.
    def __init__(self, value):
        try:
            self._validate(value)
        except ValueError as exc:
            del self
            raise exc
        self._value = value

    ## Validator da classe.
    #   Verifica a validade do argumento passado, lançando uma exceção
    #   no caso de ser negativa.
    #
    #   @arg        value       String a ser validada.
    #
    #   @exception  ValueError  Exceção lançada no caso de
    #                           value possuir mais de um, ou
    #                           nenhum, arroba; no caso de
    #                           value possuir caracteres
    #                           não-alfa-numéricos ou caso a
    #                           contagem de pontos esteja
    #                           incorreta.
    def _validate(self, value):
        notag = value.replace("@", "").replace(".", "")
        if len(value) == 0:
            raise ValueError(lang.DICT['EXCEPTION_INV_ML_S'])
        elif unicode.isalnum(notag) == False:
            raise ValueError(lang.DICT['EXCEPTION_INV_ML_F'])
        elif value.count('@') == 1:
            if value[value.index('@'):].count('.') < 1:
                raise ValueError(lang.DICT['EXCEPTION_INV_ML_F'])
        else:
            raise ValueError(lang.DICT['EXCEPTION_INV_ML_F'])
        
## Classe container de tipo de exercício.
#   Este tipo básico contém um inteiro que representa um tipo de exercício.
#   Cada tipo de exercício funciona de uma forma diferente, e eles são
#   escaláveis.
class ExType(IfBaseType):
    _value = None

    ## Contrutor da classe,.
    #   Impede a criação do tipo básico para valores de entrada
    #   inválidos.
    #
    #   @arg        value       Valor de entrada, que será
    #                           armazenado no tipo básico.
    #
    #   @exception  ValueError  Será lançada no caso do valor
    #                           de entrada ser inválido.
    def __init__(self, value):
        try:
            self._validate(value)
        except ValueError as exc:
            del self
            raise exc
        self._value = value

    ## Validador da classe.
    #   Lança uma excessão no caso de value não atender aos requisitos
    #   do sistema.
    #
    #   @arg        value       Inteiro que será testado.
    #
    #   @exception  ValueError  Será lançado no caso de value
    #                           ser negativo ou não inteiro.
    def _validate(self, value):
        try: int(value)
        except ValueError: raise ValueError(lang.DICT['EXCEPTION_INV_ET_F'])

        if value <= 0:
            raise ValueError(lang.DICT['EXCEPTION_INV_ET_S'])

## Classe container de Id.
#   Este tipo básico irá armazenar um inteiro, que identifica univocamente
#   diversas estruturas dentro do sistema.
class Id(IfBaseType):
    _value = None

    ## Construtor da classe.
    #   Responsável por impedir a criação de um tipo básico com
    #   conteúdo inválido.
    #
    #   @arg        value       Inteiro a ser salvo no tipo
    #                           básico.
    #
    #   @exception  ValueError  Será lançada no caso de value
    #                           não corresponder aos requisitos
    #                           do sistema.
    def __init__(self, value):
        try:
            self._validate(value)
        except ValueError as exc:
            del self
            raise exc
        self._value = value

    ## Validador da classe.
    #   Lança uma exceção no caso do valor de entrada não bater com os
    #   requisitos para um Id.
    #
    #   @arg        value       Inteiro a ser testado.
    #
    #   @exception  ValueError  Exceção a ser lançada no caso
    #                           de value não ser inteiro ou,
    #                           caso seja, negativo.
    def _validate(self, value):
        try: int(value)
        except ValueError: raise ValueError(lang.DICT['EXCEPTION_INV_ID_F'])

        if value < 0:
            raise ValueError(lang.DICT['EXCEPTION_INV_ID_S'])

## Classe container de linguagem.
#   Irá armazenar um número que corresponde à língua de preferência do
#   usuário. A relação linguagem-id será armazenada numa tabela à parte.
class Language(IfBaseType):
    _value = None

    ## Construtor da classe.
    #   Impede a criação de tipos básicos com conteúdo inválido.
    #
    #   @arg        value       Inteiro a ser armazenado.
    #
    #   @exception  ValueError  Exceção a ser lançada no caso
    #                           de value não corresponder às
    #                           expectativas.
    def __init__(self, value):
        try:
            self._validate(value)
        except ValueError as exc:
            del self
            raise exc
        self._value = value

    ## Validador da classe.
    #   Recebe um inteiro e verifica se ele pode ser utilizado como
    #   Linguagem.
    #
    #   @arg        value       Inteiro a ser analisado.
    #
    #   @exception  ValueError  Exceção a ser lançada caso
    #                           value não seja inteiro ou
    #                           seja negativo.
    def _validate(self, value):
        try: int(value)
        except ValueError: raise ValueError(lang.DICT['EXCEPTION_INV_LG_F'])

        if value < 1:
            raise ValueError(lang.DICT['EXCEPTION_INV_LG_F'])

## Classe container de Data.
#   Este tipo básico armazena uma data para os mais diversos usos.
class Date(IfBaseType):
    _value = None
    
    ## Construtor da classe.
    #   Responsável por impedir a criação de um tipo básico que não
    #   atenda aos requisitos do sistema.
    #
    #   @arg        day     Dia a ser armazenado.
    #
    #   @arg        month       Mês a ser armazenado.
    #
    #   @arg        year        Ano a ser armazenado.
    #
    #   @exception  ValueError  Exceção a ser lançada caso a
    #                           data seja inválida.
    def __init__(self, day, month, year):
        try:
            value['day'] = day
            value['month'] = month
            value['year'] = year
            self._validate(value)
        except ValueError as exc:
            del self
            raise exc
        self._value = value

    ## Validator da classe.
    #   Método que recebe um dicionário e verifica se a data nele
    #   contida é válida.
    #
    #   @arg        value       Dicionário a ser testado. Deve
    #                           conter no mínimo três campos:
    #                           year, month e day.
    #
    #   @exception  ValueError  Exceção que será lançada na
    #                           eventualidade da data inserida
    #                           ser impossível de ocorrer, ou
    #                           caso ela seja anterior a 2014.
    def _validate(self, value):
        year = value['year']
        month = value['month']
        day = value['day']

        if year < 2014:
            raise ValueError(lang.DICT['EXCEPTION_INV_DT_Y'])

        if month < 1 or month > 12:
            raise ValueError(lang.DICT['EXCEPTION_INV_DT_M'])

        if day < 1:
            raise ValueError(lang.DICT['EXCEPTION_INV_DT_D'])

        if month == 2:
            if day > 29:
                raise ValueError(lang.DICT['EXCEPTION_INV_DT_D'])
        elif month <= 7:
            if day > 30 + (1 if month % 2 else 0):
                raise ValueError(lang.DICT['EXCEPTION_INV_DT_D'])
        else:
            if day > 30 + (0 if month % 2 else 1):
                raise ValueError(lang.DICT['EXCEPTION_INV_DT_D'])

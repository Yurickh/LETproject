#encode: utf-8

## @package BaseUnit
# Base Type container.
# Este arquivo e responsável pela implementação dos tipos básicos do programa.
# Cada classe deve conter o validator, que garante que os tipos básicos são compatíveis com o formato especificado nos #requisitos.

from abc import *
import hashlib

from lang.pt_br import *

## Interface para qualquer tipo básico (Base Type) pertencente ao projeto.
#		Sua descrição implica que todos os tipos básicos devem ter um atributo _value e um método _validate.
class IfBaseType:

	## Especifica que o IfBaseType é uma classe base abstrata (abc). 
	# Isso significa que uma classe derivada pode ser instanciada se - e somente se - ela der "override" em todos os métodos e
	# propriedades abstratas.
	__metaclass__ = ABCMeta

	## Método que retorna o valor de um dado objeto.
	@property
	def value(self):
		return self._value

	## Método que fixa e valida o conteúdo de um objeto.
	@value.setter
	def value(self, aux):
		self._validate(aux)
		self._value = aux

	## Método que deleta o conteúdo de um objeto.
	@value.deleter
	def value(self):
		del self._value

	## Define que toda classe derivada terá um método _validate.
	@abstractmethod
	def _validate(self, value): pass

	## Método que compara o conteúdo de dois objetos.
	# Retorna '0' se o conteúdo for o mesmo e '1' ou '-1' caso sejam diferentes.
	def __cmp__(self, other):
		if other.value == self.value:
			return 0
		elif other.value > self.value:
			return 1
		else:
			return -1

## Classe responsável por armazenar e codificar uma string que será usada como o password pelo sistema.
class Password(IfBaseType):
	_value = None

	## Construtor da classe.
	# Responsável por validar e definir o valor do password.
	def __init__(self, value):
		try:
			self._validate(value)
		except ValueError as exc:
			del self
			raise exc
		self._value = hashlib.md5(hashlib.sha256(value).hexdigest()).hexdigest()

	## Validator da classe.
	# Responsável pela validação do password. Se o tamanho do password for menor que 6, ele irá lançar uma excessão.
	def _validate(self, value):
		if(len(value) < 6):
			raise ValueError(EXCEPTION_INV_PW_S)

	@property
	def value(self):
		return self._value

	## Dá um 'override' no método setValue() de IfBaseType para fazer o hash.
	@value.setter
	def value(self, value):
		self._validate(value)
		self._value = hashlib.md5(hashlib.sha256(value).hexdigest()).hexdigest()

## Classe responsável por armazenar uma string dada para ser usada como um nome pelo sistema.
class Name(IfBaseType):

	_value = None

	## Construtor da classe.
	# Responsável pela validação do valor no conteúdo de password.	
	def __init__(self, value):
		try:
			self._validate(value)
		except ValueError as exc:
			del self
			raise exc
		self._value = value

	## Validator da classe.
	# Responsável pela validação do nome. Se o número de caracteres for maior que 32, se for NULL ou se contém caracteres não 
	# alfanuméricos, irá lançar uma excessão.
	def _validate(self, value):
		if len(value) > 32:
			raise ValueError(EXCEPTION_INV_NM_B)
		else: 
			if len(value) == 0:
				raise ValueError(EXCEPTION_INV_NM_S)
			else:
				if unicode.isalnum(value.replace(" ", "")) == False:
					raise ValueError(EXCEPTION_INV_NM_F)

## Classe responsável por armazenar um número dado que será usado como um registro dos usuários no sistema.	
class Matric(IfBaseType):

	_value = None

	## Construtor da classe.
	# Responsavel por validar e definir o valor de matric.
	def __init__(self, value):
		try:
			self._validate(value)
		except ValueError as exc:
			del self
			raise exc
		self._value = value

	## Validator da classe.
	# Responsável por checar se o número de registro é maior do que o máximo permitido (999999999) ou menor que 1.
	def _validate(self, value):
		try: int(value)
		except ValueError: raise ValueError(EXCEPTION_INT_MT_F)

		if value > 999999999:
			raise ValueError(EXCEPTION_INV_MT_B)
		elif value < 1:
			raise ValueError(EXCEPTION_INV_MT_S)
		
## Classe responsável por armazenar textos simples, que corresponde a qualquer tipo de texto.
class PlainText(IfBaseType):
	_value = None

	## Construtor da classe.
	# Responsável por validar e definir um valor (conteúdo) de um texto.
	def __init__(self, value):

		try:
			self._validate(value)
		except ValueError as exc:
			del self
			raise exc
		self._value = value

	## Validator da classe.
	# É responsável por validar o texto. Se o comprimento do texto for maior que 1024 caracteres, irá lançar uma excessão.
	def _validate(self, value):
		if len(value) > 1024:
			raise ValueError(EXCEPTION_INV_PT_B)

## Classe responsável por armazenar o id do Campus.
class Campus(IfBaseType):

	_value = None

	## Construtor da classe.
	# Responsável por validar e definir o id de campus.
	def __init__(self, value):
		try:
			self._validate(value)
		except ValueError as exc:
			del self
			raise exc
		self._value = value

	## Validator da classe.
	# Responsável por validar o id do campus. Se o número do id do campus for menor que '0', ele irá lançar uma excessão.
	def _validate(self, value):
		try: int(value)
		except ValueError: raise ValueError(EXCEPTION_INV_CP_F)

		if value <= 0:
			raise ValueError(EXCEPTION_INV_CP_S)

## Classe responsável por armazenar o sexo do usuário.
class Sex(IfBaseType):
	_value = None
	
	## Construtor da classe.
	# Responsável por validar e definir o conteúdo em sexo.
	def __init__(self, value):
		try:
			self._validate(value)
		except ValueError as exc:
			del self
			raise exc
		self._value = value

	## Validato da classe.
	# Responsável por validar o contúdo em sexo. Se o caractere for diferente de 'm', 'M', 'f' e 'F', irá lançar uma excessão.
	def _validate(self, value):
		if value != 'm' and value != 'M' and value != 'f' and value != 'F':
			raise ValueError(EXCEPTION_INV_SX_F)

## Classe responsável por armazenar uma dada string que será usada como um link.
class Link(IfBaseType):
	_value = None

	## Construtor da classe.
	# Responsável por validar e definir o valor (conteúdo) de um link.
	def __init__(self, value):
		try:
			self._validate(value)
		except ValueError as exc:
			del self
			raise exc
		self._value = value

	## Validator da classe.
	# Responsável por validar um link. Se o comprimento do link for 0, ou se tem caracteres não alfanumérico, irá lançar uma escessão.
	def _validate(self, value):
		if len(value) == 0:
			raise ValueError(EXCEPTION_INV_LK_S)
		elif unicode.isalnum(value.replace("/", "")) == False and len(value.replace("/", "")) > 0:
			raise ValueError(EXCEPTION_INV_LK_F)

## Classe responsável por armazenar um número inteiro dado que representará uma nota.
class Grades(IfBaseType):
	_value = None

	## Contrutor da classe.
	# Responsável por validar e fixar um valor (conteúdo) de um objeto do tipo nota.
	def __init__(self, value):
		try:
			self._validate(value)
		except ValueError as exc:
			del self
			raise exc
		self._value = value

	## Validator da classe.
	# Responsável por validar uma nota. Se o inteiro é menor que zero, ou maio que 100, irá mandar uma excessão.
	def _validate(self, value):
		try: int(value)
		except ValueError: raise ValueError(EXCEPTION_INV_GR_F)

		if value < 0:
			raise ValueError(EXCEPTION_INV_GR_S)
		elif value > 100:
			raise ValueError(EXCEPTION_INV_GR_B)

## Classe responsável por armazenar o e-mail do usuário.
class Mail(IfBaseType):
	_value = None

	## Construtor da classe.
	# Responsável por validar e definir um e-mail.
	def __init__(self, value):
		try:
			self._validate(value)
		except ValueError as exc:
			del self
			raise exc
		self._value = value

	## Validator da classe.
	# Responsável por validar "MaiL". Se o valor do conteúdo for NULL, ou se conter espaços em branco, mais de um '@' e menos de um '.'
	# depois do '@', irá lançar uma excessão.
	def _validate(self, value):
		if len(value) == 0:
			raise ValueError(EXCEPTION_INV_ML_S)
		elif unicode.isalnum(value.replace("@", "").replace(".", "")) == False:
			raise ValueError(EXCEPTION_INV_ML_F)
		elif value.count('@') == 1:
			if value[value.index('@'):].count('.') < 1:
				raise ValueError(EXCEPTION_INV_ML_F)
		else:
			raise ValueError(EXCEPTION_INV_ML_F)
		
## Classe responsável por armazenar um dado inteiro que representará um tipo de exercício.
class ExType(IfBaseType):
	_value = None

	## Contrutor da classe,.
	# Responsável por validar e definir os tipos de exercício.
	def __init__(self, value):
		try:
			self._validate(value)
		except ValueError as exc:
			del self
			raise exc
		self._value = value

	## Validator da classe.
	# Responsável por validar o tipo de exercício. Se o inteiro for zero ou menor que zero irá lançar uma excessão.
	def _validate(self, value):
		try: int(value)
		except ValueError: raise ValueError(EXCEPTION_INV_ET_F)

		if value <= 0:
			raise ValueError(EXCEPTION_INV_ET_S)

## Classe responsável por armazenar um Id.
class Id(IfBaseType):
	_value = None

	## Construtor da classe.
	# Responsável por validar e definir um e-mail.
	def __init__(self, value):
		try:
			self._validate(value)
		except ValueError as exc:
			del self
			raise exc
		self._value = value

	## Validator da classe.
	# Responsável por validar o Id. Se o número de Id for menor que 1, o validator irá lançar uma excessão.
	def _validate(self, value):
		try: int(value)
		except ValueError: raise ValueError(EXCEPTION_INV_ID_F)

		if value < 1:
			raise ValueError(EXCEPTION_INV_ID_S)

## Classe resonsável por armazenar a linguagem do sistema.
class Language(IfBaseType):
	_value = None

	## Construtor da classe.
	# Responsável por validar e definir a linguagem.
	def __init__(self, value):
		try:
			self._validate
		except ValueError as exc:
			del self
			raise exc
		self._value = value

	## Validator da classe.
	# Responsável pela validação da linguagem. Se for menor que 1, o validator irá lançar uma excessão.
	def _validate(self, value):
		try: int(value)
		except ValueError: raise ValueError(EXCEPTION_INV_LG_F)

		if value < 1:
			raise ValueError(EXCEPTION_INV_LG_F)

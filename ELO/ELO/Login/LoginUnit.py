from abc import *

class IfUiLogin:

	__metaclass__ = ABCMeta

	@abstractmethod
	def run(): pass

class NegUiLogin:

	__metaclass__ = ABCMeta

	@abstractmethod
	def validate(username, password): pass

class UiLogin(IfInterLogin):
	
	busLogin = None
	
	def run():
		"""1. Criar a página. //django
		2. Receber dados. // django
		3. Chamar negócio e validar dados. <--
			3.1 False:
				Notificar e retornar a 2. <--
			3.2 True:
				Cria sessão e continua. //django"""

	def setBus(self, busClass):
		self.busLogin = busClass
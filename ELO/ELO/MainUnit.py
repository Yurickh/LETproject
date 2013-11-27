from LoginUnit import *

class Factory():
	__ui = None
	__bus = None
	__pers = None

	def runLogin(self, request):
		if not self.__ui is IfUiLogin:
			self.__ui = UiLogin()
			self.__bus = BusLogin()
			self.__pers = PersLogin()
	
		

from ..Login.LoginUnit import UiLogin, StubLogin

class Factory(object):
	
	def run(self):
		ilogin = UiLogin()
		slogin = StubLogin()

		ilogin.setBus(slogin)

		return ilogin.run()
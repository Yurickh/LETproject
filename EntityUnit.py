#coding: utf-8

from baseUnit import *
from abc import *

EXCEPTION_INV_USR_NM = "LOL"
EXCEPTION_INV_USR_PW = "LO;2"
EXCEPTION_INV_ADM = "FODEA-SE"
EXCEPTION_INV_PRF = "DIOWJDOWJ"
EXCEPTION_INV_PRF_MT = "UHAHASUA"

class User:
	__metaclass__ = ABCMeta

	__instantiable = abstractproperty()

	def getName(self):
		return self._name

	def getPassword(self):
		return self._password

	def setName(self, name):
		if isinstance(name, Name):
			self._name = name
		else:
			raise ValueError(EXCEPTION_INV_USR_NM)

	def setPassword(self, password):
		if isinstance(password, Password):
			self._password = password
		else:
			raise ValueError(EXCEPTION_INV_USR_PW)

	def delName(self):
		del self._name

	def delPassword(self):
		del self._password

	_name = property(getName, setName, delName)
	_password = property(getPassword, setPassword, delPassword)

class Adm(User):
	_User__instantiable = True

	def __init__(self, name, password):
		if isinstance(name, Name):
			_name = name
			if isinstance(password, Password):
				_password = password
				error = False
			else:
				error = True
		else:
			error = True

		if error == True:
			del self
			raise ValueError(EXCEPTION_INV_ADM)

class Professor(User):
	_User__instantiable = True

	def __init__(self, name, password, matric):
		if isinstance(name, Name):
			_name = name
			
			if isinstance(password, Password):
				_password = password

				if isinstance(matric, Matric):
					__matric = matric
					error = False
				else:
					error = True
			else:
				error = True
		else:
			error = True
		

		if error == True:
			del self
			raise ValueError(EXCEPTION_INV_PRF)

	def getMatric(self):
		return self.__matric

	def setMatric(self, matric):
		if isinstance(matric, Matric):
			self.__matric = matric
		else:
			raise ValueError(EXCEPTION_INV_PRF_MT)

	def delMatric(self):
		del __matric

	__matric = property(getMatric, setMatric, delMatric)
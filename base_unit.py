"""@package docstring
Base Type container.

This file is responsible for the implementation of the base types of our program. Each class shall contain a validator that will guarantee that the base type is compatible with the requirements.
"""

from macros_pt_br import *
import hashlib

class Password:
	""" Class responsible for storing and hashing a given string to be used as a password by the system.
	"""
	__value = None

	def __init__(self, value):
		""" Class constructor.

			It is responsible for the validation and setting of the value of the password.
		"""
		self.__validate(value)
		self.__value = hashlib.md5(hashlib.sha256(value).hexdigest()).hexdigest()

	def __validate(self, value):
		if len(value) < 6:
			raise ValueError(EXCEPTION_000)

	def setValue(self, value):
		self.__validate(value)
		self.__value = hashlib.md5(hashlib.sha256(value).hexdigest()).hexdigest()

	def getValue(self):
		return self.__value

class Matric:
	""" Class responsible for storing a given number to be used as a registry by the users of the system
	"""	
	__value = None

	def __init__(self, value):
		""" Class constructor.

			It is responsible for the validation and setting of the value of the matric.
		"""
		self.__validate(value)
		self.__value = value

	def __validate(self, value):
		""" Class validator.

			It is responsible for checking if the registry number is bigger than the max allowed (999999999) or smaller than 1.

		"""
		if value > 999999999:
			raise ValueError(EXCEPTION_004)
		elif value < 1:
			raise ValueError(EXCEPTION_005)
		
	def setValue(self, value):
		self.__validate(value)
		self.__value = value

	def getValue(self):
		return self.__value

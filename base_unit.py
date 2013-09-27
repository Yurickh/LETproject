"""@package docstring
Base Type container.

This file is responsible for the implementation of the base types of our program. Each class shall contain a validator that will guarantee that the base type is compatible with the requirements.
"""

from macros_pt_br import *
import hashlib
from str import *

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
		"""Class validator.
		It is responsible for the validation of the password. If the length of the password is under 6, it will raise an exception.
		"""
		if len(value) < 6:
			raise ValueError(EXCEPTION_000)

	def setValue(self, value):
		self.__validate(value)
		self.__value = hashlib.md5(hashlib.sha256(value).hexdigest()).hexdigest()

	def getValue(self):
		return self.__value

class Name:
	""" Class responsible for storing a given string to be used as a name by the system.
	"""
	__value = None
	
	def __init__(self, value):
		""" Class constructor.
		It is responsible for the validation of the value of the password.
		"""
		self.__validate(value)
		self.value = value
	
	def __validate(self, value):
		"""Class validator.
		It is resonsible for the validation of the name. If the name length is over 32 or is NULL or the name contains non-alphanumerical 				digits, it will raise an exception.
		"""
		if len(value) > 32:
			raise ValueError(EXCEPTION_001)
		else if len(value) == 0:
			raise ValueError(EXCEPTION_002)
		else if !isalnum(value):
			raise ValueError(EXCEPTION_003)

	def setValue(self, value):
		self.__validate(value)
		self.__value = value
	
	def getValue(self):
		return self.__value

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



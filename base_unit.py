"""@package docstring
Base Type container.

This file is responsible for the implementation of the base types of our program. Each class shall contain a validator that will guarantee that the base type is compatible with the requirements.
"""

#IMPLEMENTAR TODOS OS TIPOS BASICOS TOMANDO POR BASE O PASSWORD.

from abc import *
import hashlib

from lang.en_us import *

class IfBaseType:
	""" Interface for any Base Type on the project.
		Its description implies that all Base Types shall have a _value attribute and a _validate method.
	"""

	__metaclass__ = ABCMeta
	""" Specifies that IfBaseType is an abstract base class (abc). 
		That means that a derived class can be instantiated if - and only if - it overrides all its abstract property and methods.
	"""

	def getValue(self):
		return self._value

	def setValue(self, value):
		self._value = value

	def delValue(self):
		del self._value

	_value = abstractproperty(getValue, setValue, delValue)

	@abstractmethod
	def _validate(self, value): pass

class Password(IfBaseType):
	""" Class responsible for storing and hashing a given string to be used as a password by the system.
	"""
	_value = None

	def __init__(self, value):
		""" Class constructor.
		It is responsible for the validation and setting of the value of the password.
		"""
		try:
			self._validate(value)
		except ValueError as exc:
			del self
			raise exc
		self._value = hashlib.md5(hashlib.sha256(value).hexdigest()).hexdigest()

	def _validate(self, value):
		"""Class validator.
		It is responsible for the validation of the password. If the length of the password is under 6, it will raise an exception.
		"""
		if(len(value) < 6):
			raise ValueError(EXCEPTION_INV_PW_S)

	def setValue(self, value):
		"""Overrides the IfBaseType setValue() for the sake of hashing."""
		self._validate(value)
		self._value = hashlib.md5(hashlib.sha256(value).hexdigest()).hexdigest()

class Name:
	""" Class responsible for storing a given string to be used as a name by the system.
	"""
	_value = None
	
	def __init__(self, value):
		""" Class constructor.
		It is responsible for the validation of the value of the password.
		"""
		self._validate(value)
		self._value = value
	
	def _validate(self, value):
		"""Class validator.
		It is resonsible for the validation of the name. If the name length is over 32 or is NULL or the name contains non-alphanumerical 				digits, it will raise an exception.
		"""
		if len(value) > 32:
			raise ValueError(EXCEPTION_INV_NM_B)
		else: 
			if len(value) == 0:
				raise ValueError(EXCEPTION_INV_NM_S)
			else:
				if isalnum(value) == False:
					raise ValueError(EXCEPTION_INV_NM_F)

	def setValue(self, value):
		self._validate(value)
		self._value = value
	
	def getValue(self):
		return self._value


class Matric:
	""" Class responsible for storing a given number to be used as a registry by the users of the system
	"""	
	_value = None

	def __init__(self, value):
		""" Class constructor.

			It is responsible for the validation and setting of the value of the matric.
		"""
		self._validate(value)
		self._value = value

	def _validate(self, value):
		""" Class validator.

			It is responsible for checking if the registry number is bigger than the max allowed (999999999) or smaller than 1.

		"""
		if value > 999999999:
			raise ValueError(EXCEPTION_INV_MT_B)
		elif value < 1:
			raise ValueError(EXCEPTION_INV_MT_S)
		
	def setValue(self, value):
		self._validate(value)
		self._value = value

	def getValue(self):
		return self._value


class PlainText:
	"""Class responsible for storing plain texts, that are any kind of text.
	"""
	_value = None
	def __init__(self, value):
		""" Class contructor.
		It is responsible for the validation and setting of the value of the plain text.
		"""
		self._validate(value)
		self._value = value
	def _validate(self, value):
		"""Class validator.
		It is responsible for validating the plain text. If the length of the text is over 1024, it will raise an exception.
		"""
		if len(value) > 1024:
			raise ValueError(EXCEPTION_INV_PT_B)

	def setValue(self, value):
		self._validate(value)
		self._value = value

	def getValue(self):
		return self._value

class Campus:
	"""Class responsible for storing the id of the Campus.
	"""
	_value = None

	def __init__(self, value):
		"""Class constructor.
		It is responsible for the validation and setting of the campus id.
		"""
		self._validate(value)
		self._value = value

	def _validate(self, value):
		"""Class validator.
		It is responsible for validating the campus id. If the number of the campus is under 0, it will raise an exception.
		"""
		if value <= 0:
			raise ValueError(EXCEPTION_INV_CP_S)

	def setValue(self, value):
		self._validate(value)
		self._value = value

	def getValue(self):
		return self._value


class Sex:
	"""Class responsible for storing the sex of the user.
	"""
	_value = None

	def __init__(self, value):
		"""Class constructor.
		I is responsible for the validation and setting of the sex.
		"""
	def _validate(self, value):
		"""Class validator.
		It is responsible for the validating the sex. If the character is different than 'm', 'M', 'f' and 'F', it will raise an exception.
		"""
		if value != 'm' and value != 'M' and value != 'f' and value != 'F':
			raise ValueError(EXCEPTION_INV_SX_F)

	def setValue(self, value):
		self._validate(value)
		self._value = value

	def getValue(self):
		return self._value






























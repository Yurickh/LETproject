#coding: utf-8
import inspect

from EntityUnit import *
class TestUnit:
	
	def test(self, className, testValues):
		print "------------------------------------------"
		print "Testing " + str(className)
		print "------------------------------------------"

		def foo(string): 
			if string[0] == '_': return None
			else: return string

		classType = globals()[className]
		attrList = filter(foo, dir(classType))

		arguments = inspect.getargspec(classType.__init__).args
		arguments.pop(0)

		initArguments = []

		for elem in arguments:
			initArguments.append(testValues[elem])
		
		try:
			testing = classType(*initArguments)
			print "No errors ocurred in the object's creation process." + str(attrList)
			for attrStr in attrList:
				value = testValues[attrStr]
				attr = getattr(testing, attrStr)
				if hasattr(value, "value"): print "Testing " + str(attrStr) + " against " + str(type(value)) + " " + str(value.value)
				if type(value) is list:
					for vval, aval in zip(value, attr):
						aval.value = vval.value
				elif type(value) is dict:
					for vval, aval in zip(value.values(), attr.values()):
						aval.value = vval.value
				else:
					attr.value = value.value
			print "No errors ocurred in the object's setValue() execution."
		except ValueError as exc:
			print exc
			return False

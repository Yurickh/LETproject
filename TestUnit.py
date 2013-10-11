#coding: utf-8

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
		
		try:
			testing = classType(*testValues)
			print "No errors ocurred in the object's creation process."
			for attrStr, value in zip(attrList, testValues):
				attr = getattr(testing, attrStr)
				attr.value = value
			print "No errors ocurred in the object's setValue() execution."
		except ValueError as exc:
			print exc
			return False
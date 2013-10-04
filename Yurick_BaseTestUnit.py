from baseUnit import *

class TestUnit:
	
	def test(self, info, classtype):
		print "Testing " + info + " into an " + classtype

		classType = globals()[classtype]

		try:
			testing = classType(info);
			print "No errors ocurred in the object's creation process."
			testing.setValue(info);
			print "No errors ocurred in the object's setValue() execution."
		except ValueError as exc:
			print exc
			return False
		else:
			if classtype == "Password":
				if hashlib.md5(hashlib.sha256(info).hexdigest()).hexdigest() != testing.getValue():
					print "Error: Invalid getValue() return expression."
				else:
					print "No error ocurred in the object's getValue() execution."
			else:
				if info != testing.getValue():
					print "Error: Invalid getValue() return expression."
				else:
					print "No errors ocurred in the object's getValue() execution."


def main():
	index = {
		'Password':['abcde','Yurick Hauschild_@']
		}

	for cls, cur in index.iteritems():
		for ans in cur:
			TestUnit().test(ans, cls)


main()
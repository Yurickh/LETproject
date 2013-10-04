from baseUnit import *

class Test:
	__value = None

	def _test(testValue, classtype):

		print "Testando o" + classtype.__class__.__name__ + ":"
		try: 
			__value = classtype(testValue)
			classtype.setValue(__value)
			aux = classtype.getValue(__value)
			if aux != testValue:
				raise ValueError(EXCEPTION_TEST_INV_GET)
		except ValueError as exc:
			print EXCEPTION_TEST_PREFIX + exc

def main():
	

main()

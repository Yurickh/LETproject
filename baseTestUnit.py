from baseUnit import *
BIG_WORD = "aufnKENFKJAGLANGLIERGBLIAEURGBLIBIBibiubagaiurbgpaurbglaurbgluabwerbuygewranrgabrfgbklfsdagbrablrkjblkbglksfbglsdbfglkdbjgkhslkgjsdlkfhgsldkjfglksjdhfgliutgrurgukrkurg ieur iseu  m gjsenrgsnerglse ikansrnfgakwurengueniusenuseinoiseurngusierngolurseingeiurglnsegbrablrkjblkbglksfbglsdbfglkdbjgkhslkgjsdlkfhgsldkjfglksjdhfgliutgrurgukrkurg ieur iseu  m gjsenrgsnerglse ikansrnfgakwurengueniusenuseinoiseurngusierngolurseingeiurglnsegbrablrkjblkbglksfbglsdbfglkdbjgkhslkgjsdlkfhgsldkjfglksjdhfgliutgrurgukrkurg ieur iseu  m gjsenrgsnerglse ikansrnfgakwurengueniusenuseinoiseurngusierngolurseingeiurglnsegbrablrkjblkbglksfbglsdbfglkdbjgkhslkgjsdlkfhgsldkjfglksjdhfgliutgrurgukrkurg ieur iseu  m gjsenrgsnerglse ikansrnfgakwurengueniusenuseinoiseurngusierngolurseingeiurglnsegbrablrkjblkbglksfbglsdbfglkdbjgkhslkgjsdlkfhgsldkjfglksjdhfgliutgrurgukrkurg ieur iseu  m gjsenrgsnerglse ikansrnfgakwurengueniusenuseinoiseurngusierngolurseingeiurglnsegbrablrkjblkbglksfbglsdbfglkdbjgkhslkgjsdlkfhgsldkjfglksjdhfgliutgrurgukrkurg ieur iseu  m gjsenrgsnerglse ikansrnfgakwurengueniusenuseinoiseurngusierngolurseingeiurglnsegbrablrkjblkbglksfbglsdbfglkdbjgkhslkgjsdlkfhgsldkjfglksjdhfgliutgrurgukrkurg ieur iseu  m gjsenrgsnerglse ikansrnfgakwurengueniusenuseinoiseurngusierngolurseingeiurglnse	"
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
	test = Test()
	
#Testing Passsword
#valid
	print "Testing 'Oieusouogoku' for the class Password."
	test._test(Password, "Oieusouogoku")
	print "Testing '123 a´aed' for the class Password."
	test._test(Password, "123 a´aed")

#invalid
	print "Testing 'None' for the class Password."
	test._test(Password, "")
	print"Testing 'abc' for the class Password."
	test._test(Password, "abc")

#testing Name
#valid
	print "Testing 'Joao Calmon Anisio Teixeira' for the class Name."
	test._test(Name, "Joao Calmon Anisio Teixeira")

#invalid
	print "Testing 'Joao Calmon Anisio Teixeira Icc Sul Icc Norte' for the class Name."
	test._test(Name, "Joao Calmon Anisio Teixeira Icc Sul Icc Norte")
	print "Testing 'Abigail 123 ~´'[{' for the class Name."
	test._test(Name, "Abigail 123 ~´'[{")
	print "Testing 'Joao Calmon Anisio Teixeira Icc Sul Icc Norte }}' for the class Name.'
	test._test(Name, "Joao Calmon Anisio Teixeira Icc Sul Icc Norte }}")

#testing Matric
#valid
	print "Testing '2' for the class Matric."
	test._test(Matric, 2)
	print "Testing '999999' for the class Matric."
	test._test(Matric, 999999)
#invalid
	print "Testing '9999999999999' for the class Matric."
	test._test(Matric, 9999999999999)
	print "Testin '0' for the class Matric."
	test._test(Matric, 0)

#testing PlainText
#valid
	print "Testing 'Oi? Ele sincronizou com a coisa la. Baixa a master pra ca! Nao, sua master ta aqui.' for the class PlainText."
	test._test(PlainText, "Oi? Ele sincronizou com a coisa la. Baixa a master pra ca! Nao, sua master ta aqui.")


#invalid
	print "Testing 'BIG_WORD' for the class PlainText."
	test._test(PlainText, BIG_WORD)

#testing Campus
#valid
	print "Testing '3' for the class Campus."
	test._test(Campus, 3)
#invalid
	print "Testing '0' for the class Campus."
	test._test(Campus, 0)

#testing
#valid
	print "Testing '' for the class 
#invalid









main()

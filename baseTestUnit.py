from baseUnit import *
BIG_WORD = "aufnKENFKJAGLANGLIERGBLIAEURGBLIBIBibiubagaiurbgpaurbglaurbgluabwerbuygewranrgabrfgbklfsdagbrablrkjblkbglksfbglsdbfglkdbjgkhslkgjsdlkfhgsldkjfglksjdhfgliutgrurgukrkurg ieur iseu  m gjsenrgsnerglse ikansrnfgakwurengueniusenuseinoiseurngusierngolurseingeiurglnsegbrablrkjblkbglksfbglsdbfglkdbjgkhslkgjsdlkfhgsldkjfglksjdhfgliutgrurgukrkurg ieur iseu  m gjsenrgsnerglse ikansrnfgakwurengueniusenuseinoiseurngusierngolurseingeiurglnsegbrablrkjblkbglksfbglsdbfglkdbjgkhslkgjsdlkfhgsldkjfglksjdhfgliutgrurgukrkurg ieur iseu  m gjsenrgsnerglse ikansrnfgakwurengueniusenuseinoiseurngusierngolurseingeiurglnsegbrablrkjblkbglksfbglsdbfglkdbjgkhslkgjsdlkfhgsldkjfglksjdhfgliutgrurgukrkurg ieur iseu  m gjsenrgsnerglse ikansrnfgakwurengueniusenuseinoiseurngusierngolurseingeiurglnsegbrablrkjblkbglksfbglsdbfglkdbjgkhslkgjsdlkfhgsldkjfglksjdhfgliutgrurgukrkurg ieur iseu  m gjsenrgsnerglse ikansrnfgakwurengueniusenuseinoiseurngusierngolurseingeiurglnsegbrablrkjblkbglksfbglsdbfglkdbjgkhslkgjsdlkfhgsldkjfglksjdhfgliutgrurgukrkurg ieur iseu  m gjsenrgsnerglse ikansrnfgakwurengueniusenuseinoiseurngusierngolurseingeiurglnsegbrablrkjblkbglksfbglsdbfglkdbjgkhslkgjsdlkfhgsldkjfglksjdhfgliutgrurgukrkurg ieur iseu  m gjsenrgsnerglse ikansrnfgakwurengueniusenuseinoiseurngusierngolurseingeiurglnse	"
class Test:
	__value = None

	def test(self, testValue, classtype):

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
	test.test(Password, "Oieusouogoku")
	print "Testing '123 a´aed' for the class Password."
	test.test(Password, "123 a´aed")

#invalid
	print "Testing 'None' for the class Password."
	test._test(Password, "")
	print"Testing 'abc' for the class Password."
	test.test(Password, "abc")

#testing Name
#valid
	print "Testing 'Joao Calmon Anisio Teixeira' for the class Name."
	test.test(Name, "Joao Calmon Anisio Teixeira")

#invalid
	print "Testing 'Joao Calmon Anisio Teixeira Icc Sul Icc Norte' for the class Name."
	test.test(Name, "Joao Calmon Anisio Teixeira Icc Sul Icc Norte")
	print "Testing 'Abigail 123 ~´'[{' for the class Name."
	test.test(Name, "Abigail 123 ~´'[{")
	print "Testing 'Joao Calmon Anisio Teixeira Icc Sul Icc Norte }}' for the class Name.'
	test.test(Name, "Joao Calmon Anisio Teixeira Icc Sul Icc Norte }}")

#testing Matric
#valid
	print "Testing '2' for the class Matric."
	test.test(Matric, 2)
	print "Testing '999999' for the class Matric."
	test.test(Matric, 999999)
#invalid
	print "Testing '9999999999999' for the class Matric."
	test.test(Matric, 9999999999999)
	print "Testin '0' for the class Matric."
	test.test(Matric, 0)

#testing PlainText
#valid
	print "Testing 'Oi? Ele sincronizou com a coisa la. Baixa a master pra ca! Nao, sua master ta aqui.' for the class PlainText."
	test.test(PlainText, "Oi? Ele sincronizou com a coisa la. Baixa a master pra ca! Nao, sua master ta aqui.")


#invalid
	print "Testing 'BIG_WORD' for the class PlainText."
	test.test(PlainText, BIG_WORD)

#testing Campus
#valid
	print "Testing '3' for the class Campus."
	test.test(Campus, 3)
#invalid
	print "Testing '0' for the class Campus."
	test.test(Campus, 0)

#testing
#valid
	print "Testing '' for the class 
#invalid





#testing Mail
#valid
	print "Testing a valid email."
	test.test(Mail, "testando@hotmail.com")
#invalid
	print "Testing an email with a blank space."
	test.test(Mail, "arroba @hotmail.com")
	print "Testing a null email"
	test.test(Mail, None)
	print "Testing an email with more than one '@'."
	test.test(Mail, "arroba@@hotmail.com")
	print "Testing an email with less than one '.'."
	test.test(Mail, "fernando@gmailcom")

#testing grades
#valid 
	print "Testing a valid grade."
	test.test(Grades, "88")
#invalid
	print "Testing a grade that is smaller than zero"
	test.test(Grades, "-45")
	print "Testing a grade that is bigger than onde hundred."
	test.test(Grades, "105")
	
#testing Id
#valid
	print "Testing a valid Id."
	test.test(Id, "15")
#invalid
	print "Testing an Id that is less than 1."
	test.test(Id, "0")

#testing language
#valid
	print "Testing valid language."
	test.test(Language, "60")
#invalid
	print "Testing language with a value less than 1"
	test.test(Language, "0")

	
	











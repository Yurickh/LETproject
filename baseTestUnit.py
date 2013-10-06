# coding: utf-8

from baseUnit import *


BIG_WORD = "aufnKENFKJAGLANGLIERGBLIAEURGBLIBIBibiubagaiurbgpaurbglaurbgluabwerbuygewranrgabrfgbklfsdagbrablrkjblkbglksfbglsdbfglkdbjgkhslkgjsdlkfhgsldkjfglksjdhfgliutgrurgukrkurg ieur iseu  m gjsenrgsnerglse ikansrnfgakwurengueniusenuseinoiseurngusierngolurseingeiurglnsegbrablrkjblkbglksfbglsdbfglkdbjgkhslkgjsdlkfhgsldkjfglksjdhfgliutgrurgukrkurg ieur iseu  m gjsenrgsnerglse ikansrnfgakwurengueniusenuseinoiseurngusierngolurseingeiurglnsegbrablrkjblkbglksfbglsdbfglkdbjgkhslkgjsdlkfhgsldkjfglksjdhfgliutgrurgukrkurg ieur iseu  m gjsenrgsnerglse ikansrnfgakwurengueniusenuseinoiseurngusierngolurseingeiurglnsegbrablrkjblkbglksfbglsdbfglkdbjgkhslkgjsdlkfhgsldkjfglksjdhfgliutgrurgukrkurg ieur iseu  m gjsenrgsnerglse ikansrnfgakwurengueniusenuseinoiseurngusierngolurseingeiurglnsegbrablrkjblkbglksfbglsdbfglkdbjgkhslkgjsdlkfhgsldkjfglksjdhfgliutgrurgukrkurg ieur iseu  m gjsenrgsnerglse ikansrnfgakwurengueniusenuseinoiseurngusierngolurseingeiurglnsegbrablrkjblkbglksfbglsdbfglkdbjgkhslkgjsdlkfhgsldkjfglksjdhfgliutgrurgukrkurg ieur iseu  m gjsenrgsnerglse ikansrnfgakwurengueniusenuseinoiseurngusierngolurseingeiurglnsegbrablrkjblkbglksfbglsdbfglkdbjgkhslkgjsdlkfhgsldkjfglksjdhfgliutgrurgukrkurg ieur iseu  m gjsenrgsnerglse ikansrnfgakwurengueniusenuseinoiseurngusierngolurseingeiurglnse	"

class Test:
	__value = None

	def test(self, classtype, testValue):

		try: 
			self.__value = classtype(testValue)
			self.__value.setValue(testValue)
			aux = self.__value.getValue()
			if aux != testValue: 
				raise ValueError(EXCEPTION_TEST_INV_GET)
		except ValueError as exc:
			print EXCEPTION_TEST_PREFIX
			print exc

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
	test.test(Password, "")
	print"Testing 'abc' for the class Password."
	test.test(Password, "abc")
	print " "

#testing Name
#valid
	print "Testing 'Joao Calmon Anisio Teixeira' for the class Name."
	test.test(Name, "Joao Calmon Anisio Teixeira")

#invalid
	print "Testing 'Joao Calmon Anisio Teixeira Icc Sul Icc Norte' for the class Name."
	test.test(Name, "Joao Calmon Anisio Teixeira Icc Sul Icc Norte")
	print "Testing 'Abigail 123 [{' for the class Name."
	test.test(Name, "Abigail 123 [{")
	print "Testing 'Joao Calmon Anisio Teixeira Icc Sul Icc Norte ]]' for the class Name."
	test.test(Name, "Joao Calmon Anisio Teixeira Icc Sul Icc Norte ]]")
	print " "

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
	print " "

#testing PlainText
#valid
	print "Testing 'Oi? Ele sincronizou com a coisa la. Baixa a master pra ca! Nao, sua master ta aqui.' for the class PlainText."
	test.test(PlainText, "Oi? Ele sincronizou com a coisa la. Baixa a master pra ca! Nao, sua master ta aqui.")


#invalid
	print "Testing 'BIG_WORD' for the class PlainText."
	test.test(PlainText, BIG_WORD)
	print " "

#testing Campus
#valid
	print "Testing '3' for the class Campus."
	test.test(Campus, 3)

#invalid
	print "Testing '0' for the class Campus."
	test.test(Campus, 0)
	print " "

#testing Sex
	for  asc in range(0,127):
		print "Testing " + str(chr(asc)) + " for the class Sex."
		test.test(Sex, chr(asc))
	print " "
	
#testing Link
#valid
	print "Testing 'exercicios/bankai' for the class Link."
	test.test(Link, "exercicios/bankai")

#invalid
	print "Testing 'None' for the class Link."
	test.test(Link, "")
	print "Testing 'oi eu sou o goku.huehue.br' for the class Link."
	test.test(Link, "oi eu sou o goku.huehue.br")
	print "Testing 'Estástríngtêmcarácterêsacentuádos' for the class Link."
	test.test(Link, "Estástríngtêmcarácterêsacentuádos")
	print " "


#testing Mail
#valid
	print "Testing 'testando@hotmail.com' for the class Mail."
	test.test(Mail, "testando@hotmail.com")
#invalid
	print "Testing 'arroba @hotmail.com' for the class Mail."
	test.test(Mail, "arroba @hotmail.com")
	print "Testing '' for the clas Mail"
	test.test(Mail, "")
	print "Testing 'arroba@@hotmail.com' for the class Mail."
	test.test(Mail, "arroba@@hotmail.com")
	print "Testing 'fernando@gmailcom' for the class Mail."
	test.test(Mail, "fernando@gmailcom")

#testing grades
#valid 
	print "Testing '88' for the class grade."
	test.test(Grades, 88)
#invalid
	print "Testing '-45' for the class Grade"
	test.test(Grades, -45)
	print "Testing '105' for the class Grade."
	test.test(Grades, 105)
	
#testing Id
#valid
	print "Testing '15' for the class Id."
	test.test(Id, 15)
#invalid
	print "Testing '0' for the class Id."
	test.test(Id, 0)

#testing language
#valid
	print "Testing '60' for the class language."
	test.test(Language, 60)
#invalid
	print "Testing '0' for he class language."
	test.test(Language, 0)

#testing ExType
#valid
	print "Testing '' for the class ExType."
	test.test(ExType, 5)

#invalid
	print "Testing '0' for the class ExType."
	test.test(ExType, 0)
	print "Testing '-2' for the class ExType."
	test.test(ExType, -2)
	print " "
main()

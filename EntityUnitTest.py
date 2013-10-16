#coding: utf-8

from EntityUnit import *
from TestUnit import *

def main():
	index = { 
		"Professor": [{'name': "Renato", 'password': "123456", 'matric': "120021471", 'bios': "Um samurai aposentado que decidiu estudar para ser um professor de física pelo desejo de ajudar as suas ex-vítimas a passarem no vestibular", 'campus': Campus(2), 'courses': courses(2), 'avatar': "teste/teste2", 'sex': "M"}]
	}

	valid = invalid = 0
	for cls in index:
		for ans in index[cls]:
			if TestUnit().test(cls, ans):
				valid += 1
			else:
				invalid += 1

	print "\nFinished testing."
	print str(valid) + " valid assertives found."
	print str(invalid) + " invalid assertives found."

main()

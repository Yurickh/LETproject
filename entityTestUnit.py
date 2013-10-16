#coding: utf-8

from TestUnit import *

def main():
	index = {
		'Student'	:[{'name': Name('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Link('soumaisfoda/queo/kira'), 'email': Mail('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Grades(10)}, 'interests': PlainText('Interessado no Death Note'), 'language': Language(2)}],
	#		{'name': ,'password': ,'matric': ,'bios': ,'campus': , 'courses': , 'avatar': , 'email': , 'sex': , 'grades': , 'interests': , 'language': },
	#		{'name': ,'password': ,'matric': ,'bios': ,'campus': , 'courses': , 'avatar': , 'email': , 'sex': , 'grades': , 'interests': , 'language': },
	#		{'name': ,'password': ,'matric': ,'bios': ,'campus': , 'courses': , 'avatar': , 'email': , 'sex': , 'grades': , 'interests': , 'language': }],

	#	'Courses'	:[[Name("Will Smith"), Id(2), [Id(2), Id(2)], [Id(2), Id(2)]], [Name("Hahaha"), Id(2), [Id(2), Id(2)], [Id(2), Id(2)]], [Name("Ajania"), Id(2), [Id(2), Id(2)], [Id(2), Id(2)]], [Name("hei"), Id(2), [Id(2), Id(2)], [Id(2), Id(2)]]]
		'Professor'     : [{'name': Name('Renato'), 'password': Password('123456'), 'matric': Matric(120021471), 'bios': PlainText('Um samurai aposentado que decidiu estudar para ser um professor de física pelo desejo de ajudar as suas ex-vítimas a passarem no vestibular'), 'campus': Campus(2), 'courses': [Id(4), Id(8)], 'avatar': Link('teste/teste2'), 'sex': Sex('M')}, 

				{'name': Password('Renato'), 'password': Password('123456'), 'matric': Matric(120021471), 'bios': PlainText('Um samurai aposentado que decidiu estudar para ser um professor de física pelo desejo de ajudar as suas ex-vítimas a passarem no vestibular'), 'campus': Campus(2), 'courses': [Id(4), Id(8)], 'avatar': Link('teste/teste2'), 'sex': Sex('M')},

				 {'name': Name('Renato'), 'password': Link('123456'), 'matric': Matric(120021471), 'bios': PlainText('Um samurai aposentado que decidiu estudar para ser um professor de física pelo desejo de ajudar as suas ex-vítimas a passarem no vestibular'), 'campus': Campus(2), 'courses': [Id(4), Id(8)], 'avatar': Link('teste/teste2'), 'sex': Sex('M')}, 

				{'name': Name('Renato'), 'password': Password('123456'), 'matric': Campus(120021471), 'bios': PlainText('Um samurai aposentado que decidiu estudar para ser um professor de física pelo desejo de ajudar as suas ex-vítimas a passarem no vestibular'), 'campus': Campus(2), 'courses': [Id(4), Id(8)], 'avatar': Link('teste/teste2'), 'sex': Sex('M')},

				{'name': Name('Renato'), 'password': Password('123456'), 'matric': Matric(120021471), 'bios': Name('Um samurai'), 'campus': Campus(2), 'courses': [Id(4), Id(8)], 'avatar': Link('teste/teste2'), 'sex': Sex('M')},

				{'name': Name('Renato'), 'password': Password('123456'), 'matric': Matric(120021471), 'bios': PlainText('Um samurai aposentado que decidiu estudar para ser um professor de física pelo desejo de ajudar as suas ex-vítimas a passarem no vestibular'), 'campus': [Id(2), Id(7)], 'courses': [Id(4), Id(8)], 'avatar': Link('teste/teste2'), 'sex': Sex('M')},

				{'name': Name('Renato'), 'password': Password('123456'), 'matric': Matric(120021471), 'bios': PlainText('Um samurai aposentado que decidiu estudar para ser um professor de física pelo desejo de ajudar as suas ex-vítimas a passarem no vestibular'), 'campus': Campus(2), 'courses': Campus(2), 'avatar': Link('teste/teste2'), 'sex': Sex('M')},

				{'name': Name('Renato'), 'password': Password('123456'), 'matric': Matric(120021471), 'bios': PlainText('Um samurai aposentado que decidiu estudar para ser um professor de física pelo desejo de ajudar as suas ex-vítimas a passarem no vestibular'), 'campus': Campus(2), 'courses': [Id(4), Id(8)], 'avatar': Name('teste2'), 'sex': Sex('M')},

				{'name': Name('Renato'), 'password': Password('123456'), 'matric': Matric(120021471), 'bios': PlainText('Um samurai aposentado que decidiu estudar para ser um professor de física pelo desejo de ajudar as suas ex-vítimas a passarem no vestibular'), 'campus': Campus(2), 'courses': [Id(4), Id(8)], 'avatar': Link('teste/teste2'), 'sex': Name('M')}]
	}

	valid = invalid = 0
	for cls in index:
		for ans in index[cls]:
			if TestUnit().test(cls, ans):
				valid += 1
			else:
				invalid += 1

main()

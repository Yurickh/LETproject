#coding: utf-8

from TestUnit import *

def main():
	index = {
		'Student'	:[{'name': Name('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Link('soumaisfoda/queo/kira'), 'email': Mail('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Grades(10)}, 'interests': PlainText('Interessado ao Death Note'), 'language': Language(2)},
				{'name': Name('Lauriet Lindsaw taylor'),'password': Name('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Link('soumaisfoda/queo/kira'), 'email': Mail('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Grades(10)}, 'interests': PlainText('Interessado no Death Note'), 'language': Language(2)},
				{'name': Password('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Link('soumaisfoda/queo/kira'), 'email': Mail('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Grades(10)}, 'interests': PlainText('Interessado no Death Note'), 'language': Language(2)},
				{'name': Name('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': PlainText('string'),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Link('soumaisfoda/queo/kira'), 'email': Mail('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Grades(10)}, 'interests': PlainText('Interessado no Death Note'), 'language': Language(2)},
				{'name': Name('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Mail('loololo@morte.gg'), 'courses': [Id(2), Id(4)], 'avatar': Link('soumaisfoda/queo/kira'), 'email': Mail('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Grades(10)}, 'interests': PlainText('Interessado no Death Note'), 'language': Language(2)},
				{'name': Name('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Campus(2), 'email': Mail('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Grades(10)}, 'interests': PlainText('Interessado no Death Note'), 'language': Language(2)},
				{'name': Name('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Link('soumaisfoda/queo/kira'), 'email': Mail('loololo@morte.gg'), 'sex': Id(2), 'grades': {'Inteligencia' : Grades(10)}, 'interests': PlainText('Interessado no Death Note'), 'language': Language(2)},
				{'name': Name('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Link('soumaisfoda/queo/kira'), 'email': Mail('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Sex('m')}, 'interests': PlainText('Interessado no Death Note'), 'language': Language(2)},
				{'name': Name('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Link('soumaisfoda/queo/kira'), 'email': Mail('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Grades(10)}, 'interests': PlainText('Interessado no Death Note'), 'language': PlainText('bla')},
				{'name': Name('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Link('soumaisfoda/queo/kira'), 'email': Mail('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Grades(10)}, 'interests': Password('Interessado no Death Note'), 'language': Language(2)},
				{'name': Name('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Link('soumaisfoda/queo/kira'), 'email': PlainText('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Grades(10)}, 'interests': PlainText('Interessado no Death Note'), 'language': Language(2)},
				{'name': Name('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Password('soumaisfoda/queo/kira'), 'email': Mail('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Grades(10)}, 'interests': PlainText('Interessado no Death Note'), 'language': Language(2)}],

		'Courses'	:[{'name': Name('Light Yagami'), 'thisId': Id(7),'students': [Id(3), Id(4)],'modules': [Id(1), Id(8)]},
				{'name': Password('Light Yagami'), 'thisId': Id(2),'students': [Id(3), Id(4)],'modules': [Id(1), Id(8)]},
				{'name': Name('Light Yagami'), 'thisId': Campus(7),'students': [Id(3), Id(4)],'modules': [Id(1), Id(8)]},
				{'name': Name('Light Yagami'), 'thisId': Id(7),'students': [Id(3), Id(4)],'modules': [Name('oi'), Id(8)]}],

		'Lesson'	:[{'name': Name('Misa Misa'),'thisId': Id(2), 'link': Link('oenfouiwneqw/dq'), 'exercises': [Id(1), Id(3)]},
				{'name': Name('Misa Misa'),'thisId': Id(2), 'link': Name('oenfouiwneqw/dq'), 'exercises': [Id(1), Id(3)]},
				{'name': Link('Misa Misa'),'thisId': Id(2), 'link': Link('oenfouiwneqw/dq'), 'exercises': [Id(1), Id(3)]},
				{'name': Name('Misa Misa'),'thisId': Id(2), 'link': Link('oenfouiwneqw/dq'), 'exercises': [Password('1awsd'), Id(3)]},
				{'name': Name('Misa Misa'),'thisId': Campus(2), 'link': Link('oenfouiwneqw/dq'), 'exercises': [Id(1), Id(3)]}],

		'Adm'		:[{'name': Name('Yurick Hauschild'), 'password': Password('a793812b')},
				{'name': Id(2), 'password': Password('a793812b')},
				{'name': Id(2), 'password': Id(3)},
				{'name': Name('Andre Lima'), 'password': Id(3)}],

		'Professor'     : [{'name': Name('Renato'), 'password': Password('123456'), 'matric': Matric(120021471), 'bios': PlainText('Um samurai aposentado que decidiu estudar para ser um professor de física pelo desejo de ajudar as suas ex-vítimas a passarem no vestibular'), 'campus': Campus(2), 'courses': [Id(4), Id(8)], 'avatar': Link('teste/teste2'), 'sex': Sex('M')}, 
				{'name': Password('Renato'), 'password': Password('123456'), 'matric': Matric(120021471), 'bios': PlainText('Um samurai aposentado que decidiu estudar para ser um professor de física pelo desejo de ajudar as suas ex-vítimas a passarem no vestibular'), 'campus': Campus(2), 'courses': [Id(4), Id(8)], 'avatar': Link('teste/teste2'), 'sex': Sex('M')},
				{'name': Name('Renato'), 'password': Link('123456'), 'matric': Matric(120021471), 'bios': PlainText('Um samurai aposentado que decidiu estudar para ser um professor de física pelo desejo de ajudar as suas ex-vítimas a passarem no vestibular'), 'campus': Campus(2), 'courses': [Id(4), Id(8)], 'avatar': Link('teste/teste2'), 'sex': Sex('M')}, 
				{'name': Name('Renato'), 'password': Password('123456'), 'matric': Campus(120021471), 'bios': PlainText('Um samurai aposentado que decidiu estudar para ser um professor de física pelo desejo de ajudar as suas ex-vítimas a passarem no vestibular'), 'campus': Campus(2), 'courses': [Id(4), Id(8)], 'avatar': Link('teste/teste2'), 'sex': Sex('M')},
				{'name': Name('Renato'), 'password': Password('123456'), 'matric': Matric(120021471), 'bios': Name('Um samurai'), 'campus': Campus(2), 'courses': [Id(4), Id(8)], 'avatar': Link('teste/teste2'), 'sex': Sex('M')},
				{'name': Name('Renato'), 'password': Password('123456'), 'matric': Matric(120021471), 'bios': PlainText('Um samurai aposentado que decidiu estudar para ser um professor de física pelo desejo de ajudar as suas ex-vítimas a passarem no vestibular'), 'campus': [Id(2), Id(7)], 'courses': [Id(4), Id(8)], 'avatar': Link('teste/teste2'), 'sex': Sex('M')},
				{'name': Name('Renato'), 'password': Password('123456'), 'matric': Matric(120021471), 'bios': PlainText('Um samurai aposentado que decidiu estudar para ser um professor de física pelo desejo de ajudar as suas ex-vítimas a passarem no vestibular'), 'campus': Campus(2), 'courses': Campus(2), 'avatar': Link('teste/teste2'), 'sex': Sex('M')},
				{'name': Name('Renato'), 'password': Password('123456'), 'matric': Matric(120021471), 'bios': PlainText('Um samurai aposentado que decidiu estudar para ser um professor de física pelo desejo de ajudar as suas ex-vítimas a passarem no vestibular'), 'campus': Campus(2), 'courses': [Id(4), Id(8)], 'avatar': Name('teste2'), 'sex': Sex('M')},
				{'name': Name('Renato'), 'password': Password('123456'), 'matric': Matric(120021471), 'bios': PlainText('Um samurai aposentado que decidiu estudar para ser um professor de física pelo desejo de ajudar as suas ex-vítimas a passarem no vestibular'), 'campus': Campus(2), 'courses': [Id(4), Id(8)], 'avatar': Link('teste/teste2'), 'sex': Name('M')}],
	}

	valid = invalid = 0
	for cls in index:
		for ans in index[cls]:
			if TestUnit().test(cls, ans):
				valid += 1
			else:
				invalid += 1

main()

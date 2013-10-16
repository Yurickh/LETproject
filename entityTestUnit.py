#coding: utf-8

from TestUnit import *

def main():
	index = {
#		'Student'	:[{'name': Name('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Link('soumaisfoda/queo/kira'), 'email': Mail('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Grades(10)}, 'interests': PlainText('Interessado no Death Note'), 'language': Language(2)},
#						{'name': Name('Lauriet Lindsaw taylor'),'password': Name('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Link('soumaisfoda/queo/kira'), 'email': Mail('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Grades(10)}, 'interests': PlainText('Interessado no Death Note'), 'language': Language(2)},
#						{'name': Password('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Link('soumaisfoda/queo/kira'), 'email': Mail('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Grades(10)}, 'interests': PlainText('Interessado no Death Note'), 'language': Language(2)},
#						{'name': Name('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': PlainText('string'),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Link('soumaisfoda/queo/kira'), 'email': Mail('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Grades(10)}, 'interests': PlainText('Interessado no Death Note'), 'language': Language(2)},
#						{'name': Name('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Mail('loololo@morte.gg'), 'courses': [Id(2), Id(4)], 'avatar': Link('soumaisfoda/queo/kira'), 'email': Mail('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Grades(10)}, 'interests': PlainText('Interessado no Death Note'), 'language': Language(2)},
#						{'name': Name('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Campus(2), 'email': Mail('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Grades(10)}, 'interests': PlainText('Interessado no Death Note'), 'language': Language(2)},
#						{'name': Name('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Link('soumaisfoda/queo/kira'), 'email': Mail('loololo@morte.gg'), 'sex': Id(2), 'grades': {'Inteligencia' : Grades(10)}, 'interests': PlainText('Interessado no Death Note'), 'language': Language(2)},
#						{'name': Name('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Link('soumaisfoda/queo/kira'), 'email': Mail('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Sex('m')}, 'interests': PlainText('Interessado no Death Note'), 'language': Language(2)},
#						{'name': Name('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Link('soumaisfoda/queo/kira'), 'email': Mail('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Grades(10)}, 'interests': PlainText('Interessado no Death Note'), 'language': PlainText('bla')},
#						{'name': Name('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Link('soumaisfoda/queo/kira'), 'email': Mail('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Grades(10)}, 'interests': Password('Interessado no Death Note'), 'language': Language(2)},
#						{'name': Name('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Link('soumaisfoda/queo/kira'), 'email': PlainText('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Grades(10)}, 'interests': PlainText('Interessado no Death Note'), 'language': Language(2)},
#						{'name': Name('Lauriet Lindsaw taylor'),'password': Password('Eunaomateiokira'),'matric': Matric(502934),'bios': PlainText('Caracas eu sou muito burro, morri no episodio 25'),'campus': Campus(2), 'courses': [Id(2), Id(4)], 'avatar': Password('soumaisfoda/queo/kira'), 'email': Mail('loololo@morte.gg'), 'sex': Sex('M'), 'grades': {'Inteligencia' : Grades(10)}, 'interests': PlainText('Interessado no Death Note'), 'language': Language(2)}],
#	'Courses'	:[{'name': Name('Light Yagami'), 'thisId': Id(7),'students': [Id(3), Id(4)],'modules': [Id(1), Id(8)]},
#				{'name': Password('Light Yagami'), 'thisId': Id(2),'students': [Id(3), Id(4)],'modules': [Id(1), Id(8)]},
#				{'name': Name('Light Yagami'), 'thisId': Campus(7),'students': [Id(3), Id(4)],'modules': [Id(1), Id(8)]},
#				{'name': Name('Light Yagami'), 'thisId': Id(7),'students': [Id(3), Id(4)],'modules': [Name('oi'), Id(8)]}],

	'Lesson'	:[{'name': Name('Misa Misa'),'thisId': Id(2), 'link': Link('oenfouiwneqw/dq'), 'exercises': [Id(1), Id(3)]},


]

	}

	valid = invalid = 0
	for cls in index:
		for ans in index[cls]:
			if TestUnit().test(cls, ans):
				valid += 1
			else:
				invalid += 1

main()


[Name("Lauriet Lindsaw Taylor"), Password("Eumateiokirasoqn"), Matric(50135), PlainText("Caracas eu sou muito burro, morri no episodio 25"), Campus(2), [Id(2), Id(2)], Link("soumaisfoda/que/okira"), Mail("lololol@lol.gg"), Sex("m"), {"Inteligencia": Grades(10)}, PlainText("Interessado no Death Note."), Language(2)], [Name("Bugao"), Name("naoimportavaidarerrononome"), Matric(679987), PlainText("nao precisa de teste aqui, ja vai encerrar no nome."), Campus(3), [Id(2), Id(3)], Link("naoadianta/"), Mail("naotenhoemail@nunca.nao"), Sex("M"), {"Mat": Grades(3)}, PlainText("abababaaba"), Language(2)], [Name("Eu"), Password("bankai"), Password("bankai"), PlainText("hue"), Campus(2), [Id(3), Id(3)], Link("diwbwdi/"), Mail("bysbf@yb.uin"), Sex("F"), {"Mat": Grades(3)}, PlainText("jhuibibiy iy i "), Language(7)], [Name("Light"), Password("mateioL"), Matric(6786), PlainText("Eumorri"), Campus(7), [Id(4), Id(4)], Link("odethnote/nao/ta/comigo"), Mail("morrimaisleveicomigo@lol.gg"), Sex("m"), {"Ingenuidade": Grades(10)}, Language("Interessado em voltar a vida."), Language(3)]

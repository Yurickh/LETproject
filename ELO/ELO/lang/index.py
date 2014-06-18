#coding: utf-8

from importlib import import_module

## @file Arquivo de atualização e manutenção do sistema de línguas do ELO.
#	Resources disponíveis:
#		@var available_langs 	Lista das linguagens disponíveis.
#		@var lang				Classe que retorna o dicionário contendo as
#									macros utilizadas pelo sistema.

available_langs = [
				"pt_br",
				"en_us",
				]

## Função auxiliar que retorna o dicionário requisitado.
def getDICT(lang):
	for foo in available_langs:
		if lang == foo:
			lang = import_module("ELO.lang." + foo)
			return lang.DICT
	else:
		return None

## Classe responsável pela manutenção do objeto DICT.
#	O objeto DICT é um dicionário de macros desenvolvido com o propósito
#	de permitir a tradução do site para diferentes línguas.
class lang:
	
	DICT = getDICT('pt_br')

	@staticmethod
	def changeTo(lang):
		if lang in available_langs:
			DICT = getDICT(lang) 
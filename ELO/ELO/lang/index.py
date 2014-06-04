#coding: utf-8

from importlib import import_module

## @file Arquivo de atualização e manutenção do sistema de línguas do ELO.
#	Resources disponíveis:
#		@var available_langs 	Lista das linguagens disponíveis.
#		@var LANG 				Linguagem corrente do sistema.
#		@var DICT				Dicionário de tradução de macros.

available_langs = [
				"pt_br",
				"en_us",
				]

try: NAME
except NameError: #ifndef LANG
	NAME = 'pt_br'
#endif

## Retorna o dicionário correspondente à linguagem selecionada.
def getDICT(lang=NAME):
	for foo in available_langs:
		if lang == foo:
			lang = import_module("ELO.lang." + foo)
			return lang.DICT
	else:
		return None

try: DICT 
except NameError: #ifndef DICT
	DICT = getDICT(NAME)
else: #else
	if NAME in available_langs:
		if DICT.lang != NAME:
			DICT = getDICT(NAME)
	else:
		NAME = DICT.lang
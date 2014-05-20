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

## Retorna o dicionário correspondente à linguagem selecionada.
def getDICT(lang):
	for foo in available_langs:
		if lang == foo:
			lang = import_module("ELO.lang." + foo)
			LANG = foo
			return lang.DICT
	else:
		return None

try: LANG 
except NameError: #ifndef LANG
	LANG = 'pt_br'
#endif

try: DICT 
except NameError: #ifndef DICT
	DICT = getDICT(LANG)
else: #else
	if LANG in available_langs:
		if DICT.lang != LANG:
			DICT = getDICT(LANG)
	else:
		LANG = DICT.lang
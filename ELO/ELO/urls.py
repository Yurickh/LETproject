#coding: utf-8

## @file urls.py
# 	Arquivo responsável pelo redirecionamento e navegação
#	entre as páginas do site.

from django.conf.urls import patterns, url
from ELO.MainUnit import Factory

factory = Factory()

urlpatterns = patterns('', 
	## URL da home page, ou seja, a pagina de login do aluno.
	url(r'^$', factory.runHome, {'entity': 'Student'}),
 	## URL para o login do professor.
	url(r'^proflogin/?$', factory.runHome, {'entity': 'Professor'}),
	## URL para o login do administrador.
	url(r'^364fd8cdc3a35a89b7be75bc9d10ebea/?$', 
		factory.runHome, {'entity': 'Adm'}),
	## URL da pagina de perfil.
	url(r'^profile/?$', factory.runProfile, {'acctype': 'Full'}),
	## URL da pagina de logout.
	url(r'^logout/?$', factory.runLogout),
	## URL da pagina de cursos.
	url(r'^course/?$', factory.runCourse),
	## URL da pagina de administracao.
	url(r'^adm/?$', factory.runAdm),
	
)
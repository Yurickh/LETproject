#coding: utf-8

## @package Urls
# Este arquivo e responsavel por ler a URL requisitada e redirecionar o programa para a factory que irá criar um objeto para a
# criacao da pagina.
from django.conf.urls import patterns, url
from ELO.MainUnit import Factory

factory = Factory()

urlpatterns = patterns('', 
	## URL da home page, ou seja a pagina de login do aluno.
	url(r'^$', factory.runLogin, {'entity': 'Student'}),
 	## URL para o login do professor.
	url(r'^proflogin$', factory.runLogin, {'entity': 'Professor'}),
	## URL para o login do administrador.
	url(r'^364fd8cdc3a35a89b7be75bc9d10ebea$', factory.runLogin, {'entity': 'Adm'}),
	## URL da pagina de perfil.
	url(r'^profile$', factory.runProfile),
	## URL da pagina de logout.
	url(r'^logout$', factory.runLogout),
	## URL da pagina de cursos.
	url(r'^course$', factory.runCourse),
	## URL da pagina de administracao.
	url(r'^administracao$', factory.runAdm),
)

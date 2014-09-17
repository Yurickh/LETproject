#coding: utf-8

## @file urls.py
# 	Arquivo responsável pelo redirecionamento e navegação
#	entre as páginas do site.

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, url

from ELO.MainUnit import Factory
from ELO import settings

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
	## URL para mostrar assincronamente a edição de um campo de perfil.
	url(r'^assync/editfield/(?P<field>\w{3,9})/?$', 
		factory.runProfile, {'acctype' : 'Full'}),
	## URL da pagina de logout.
	url(r'^logout/?$', factory.runLogout),
	## URL da pagina de cursos.
	url(r'^course/?$', factory.runCourse),
	## URL da pagina de administracao.
	url(r'^adm/?$', factory.runAdm),
	url(r'^assync/adm-edit/(?P<action>\w{3,9})/(?P<model>\w{3,9})/?$', 
	factory.runAdm),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
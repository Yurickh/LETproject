#coding: utf-8

## @file urls.py
#   Arquivo responsável pelo processo de reconhecimento da URL requisitada
#   e correspondente chamada da função da Factory (ver MainUnit.py).
#
#   Cada pattern dentro do urlpatterns deve ter o formato:
#
#       url(r'REGEX', VIEW),
#
#   onde REGEX é a expressão regular que será utilizada para identificar
#   a URL, e VIEW o método correspondente que será chamado para processar
#   a requisição.
#
#   É importante ressaltar que o método view deverá retornar obrigatoriamente
#   um objeto do tipo HttpResponse.
#
#   Dentro do projeto, todas as views são chamadas de dentro da Factory.
#   Para mais informações, leia a documentação do MainUnit.py.

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
	## URL para o login do monitor.
	url(r'^tutorlogin/?$', factory.runHome, {'entity': 'Tutor'}),
	## URL para o login do administrador.
	url(r'^364fd8cdc3a35a89b7be75bc9d10ebea/?$', 
		factory.runHome, {'entity': 'Adm'}),
	url(r'^e50b058759a52eda8a507687887186e5/?$',
		factory.runHome, {'entity': 'God'}),
	## URL da pagina de perfil.
	url(r'^profile/?$', factory.runProfile, {'acctype': 'Full'}),
	## URL para mostrar assincronamente a edição de um campo de perfil.
	#		Requisitado pelo usuário.
	url(r'^assync/editfield/(?P<field>\w{3,9})/?$', 
		factory.runProfile, {'acctype' : 'Full'}),
	## URL da pagina de logout.
	url(r'^logout/?$', factory.runLogout),
	## URL da pagina de cursos.
	url(r'^course/(?P<courseid>\d+)/?$', factory.runCourse),
	url(r'^assync/lesson/?$', factory.runCourse),
	url(r'^adm/(?P<model>\w{3,25})/(?P<action>\w{0,9})/?$', factory.runAdm),
	url(r'^adm/(?P<model>\w{3,25})/(?P<username>\w{0,9})/searchacc?$', factory.runAdm),
	url(r'^adm/(?P<model>\w{3,25})/(?P<username>\w{0,32})/(?P<action>\w{0,9})/?$', factory.runAdm),
    url(r'^assync/lesson/?$', factory.runCourse),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

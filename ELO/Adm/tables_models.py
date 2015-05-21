#coding: utf-8

## @file tables_models.py
#	Arquivo de modelos usados no módulo de Adm.
#
#	Este arquivo é responsável por armazenar todos os modelos que serão
#	apresentados no módulo de Administração.
#
#	Modelos são abstrações de tabelas em um banco de dados.
from django.db import models

import django_tables2 as tables

class TitleColumn(tables.Column):
	def render(self, value):
	    return value

## Classe que define o padrão das colunas da tabela de estudantes.
class StudentTable(tables.Table):
	nome = TitleColumn(accessor='NAME')
	matricula = tables.Column(accessor='MATRIC')
	email = tables.Column(accessor='EMAIL')

	class Meta:
		attrs = {"id": "table1" , "class" : "paleblue"}

## Classe que define o padrão das colunas da tabela de professores e tutores.
class ProfessorTable(tables.Table):
	nome = TitleColumn(accessor='NAME')
	email = tables.Column(accessor='EMAIL')

	class Meta:
		attrs = {"id": "table1" ,"class" : "paleblue"}

## Classe que define o padrão das colunas da tabela de cursos.
class CoursesTable(tables.Table):
	matricula = tables.Column(accessor='COURMATRIC')
	nome = TitleColumn(accessor='NAME')
	professor = tables.Column(accessor='PROFESSOR')

	class Meta:
		attrs = {"id": "table1" ,"class" : "paleblue"}





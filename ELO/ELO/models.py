#coding: utf-8

## @file models.py
#	Arquivo de modelos do sistema.
#
#	Este arquivo é responsável por armazenar todos os modelos que serão
#	utilizados no sistema.
#
#	Modelos são abstrações de tabelas em um banco de dados.
#	Neste sistema, utilizamos o modelo de Triplestore. Assim, todas as tabelas
#	são definidas com três colunas essenciais: identity, field e value.
#	
#	A coluna de identity deve guardar um inteiro que identifique um objeto de
#	de forma unívoca. Funciona como uma chave primária, mas não tem relação
#	alguma com nenhum dado do objeto referenciado e deve aparecer em mais de
#	uma linha da tabela.
#
#	A coluna de field guardará o campo que está sendo referenciado. Ou seja,
#	se uma linha da tabela guarda informações sobre uma matrícula, seu field 
#	deverá	ser semelhante a "PASSWORD". Por padrão, todos os fields são
#	escritos em caixa alta.
#
#	A coluna de value armazena o valor descrito na linha. Ou seja, no exemplo
#	da matrícula, o campo value armazenaria o valor real da matrícula do
#	usuário referenciado pelo campo identity.
#
#	Dessa forma, cada linha da tabela tem o formato 'sujeito-verbo-predicado'.

from django.db import models

## Classe que define o modelo de estudante.
#	Colunas já implementadas:
#	
#	NAME: 		Identifica o nome do estudante.\n
#	PASSWORD:	Contém a hash da senha do estudante.\n
#	BIOS:		Biografia do estudante.\n
#	MATRIC:		Inteiro que representa a matrícula do estudante.\n
#	CAMPUS:		Número inteiro que representa a identity de um Campus.
#					(ver modelo Campus)\n
#	AVATAR:		Caminho completo do avatar do usuário.\n
#	EMAIL:		Email utilizado pelo estudante.\n
#	SEX:		Caractere que representa o sexo do usuário. Varia entre M/F.\n
#	INTEREST:	Lista de strings que representam o interesse do usuário.\n
#	LANGUAGE:	Código da linguagem preferida do usuário.\n
#	COURSE:		Lista de inteiros que representam identities de Cursos.
#					(ver modelo Course)
class Student(models.Model):
	identity = models.IntegerField()
	field = models.CharField(max_length=32)
	value = models.TextField()

	## Retorna os valores do aluno correspondente ao Id no banco de dados.
	def __unicode__(self):
		return u'%d : %s = %s' % (self.identity, self.field, self.value)

## Classe que define o modelo de administrador.
# 	Colunas já implementadas:
#
#	NAME:		Identifica o nome do Administrador.\n
#	PASSWORD:	Contém a hash da senha do administrador.
class Adm(models.Model):
	identity = models.IntegerField()
	field = models.CharField(max_length=32)
	value = models.TextField()

	## Retorna os valores do administrador correspondente ao Id no banco de dados.
	def __unicode__(self):
		return u'%d : %s = %s' % (self.identity, self.field, self.value)

## Classe que define o modelo de professor.
# 	Colunas já implementadas:
#
#	NAME:		Identifica o nome do Professor.\n
#	PASSWORD:	Contém a hash da senha de acesso do professor.\n
#	MATRIC:		Inteiro que representa o número de registro do professor.\n
#	BIOS:		Descrição detalhada do perfil do professor.\n
#	CAMPUS:		Inteiro que representa a identity do campus de atuação do
#					professor. (ver modelo Campus)\n
#	COURSE:		Lista de inteiros que representam os cursos associados ao
#					professor em questão. (ver modelo Course)\n
#	AVATAR:		Caminho completo do avatar do usuário.\n
#	SEX:		Caractere que representa o sexo do usuário. Varia entre M/F.\n
class Professor(models.Model):
	identity = models.IntegerField()
	field = models.CharField(max_length=32)
	value = models.TextField()

	## Retorna os valores do professor correspondente ao Id no banco de dados.
	def __unicode__(self):
		return u'%d : %s = %s' % (self.identity, self.field, self.value)

## Classe que define o modelo de deus.
#	Esta tabela sempre conterá apenas uma entrada, ou seja, este sistema é
#		monoteísta.
class God(models.Model):
	username = models.CharField(max_length=32)
	password = models.TextField()

	def __unicode__(self):
		return u'\nusername: %s\n password: %s' % (self.username, 
													   self.password)

## Classe que define o modelo de Curso.
#	Colunas já implementadas:
#
#	NAME:		Identifica o nome do curso.\n
#	ID:			Identifica univocamente o curso.\n
#	STUDENTS:	Lista de inteiros que representam os alunos associados ao
#					curso em questão. (ver modelo Student).\n
#	MODULES:	Lista de inteiros que identificam os módulos contidos no curso.
class Courses(models.Model):
	identity = models.IntegerField()
	field = models.CharField(max_length=32)
	value = models.TextField()

	def __unicode__(self):
		return u'%d : %s = %s' % (self.identity, self.field, self.value)

## Classe que define o modelo de Módulo.
#	Um módulo é o primeiro nível de divisão dentro de um curso.
#
#	Colunas já implementadas:
#
#	NAME:		Identifica o nome do módulo.\n
#	ID:			Identifica univocamente o módulo.\n
#	LESSONS:	Lista de inteiros que identificam as lições contidas dentro
#					dos módulos.
class Module(models.Model):
	identity = models.IntegerField()
	field = models.CharField(max_length=32)
	value = models.TextField()

	def __unicode__(self):
		return u'%d : %s = %s' % (self.identity, self.field, self.value)

## Classe que define o modelo de Lição.
#	Colunas já implementadas:
#
#	NAME:		Identifica o nome da lição.\n
#	ID:			Identifica univocamente o módulo.\n
#	LINK:		Caminho de arquivo para o html a ser parseado.\n
#	EXERCISES:	Lista de ínteiros que representam os exercícios associados
#					à lição correspondente.\n
class Lesson(models.Model):
	identity = models.IntegerField()
	field = models.CharField(max_length=32)
	value = models.TextField()

	def __unicode__(self):
		return u'%d : %s = %s' % (self.identity, self.field, self.value)

## Classe que define o modelo de exercício.
#	Colunas já implementadas:
#
#	ID:			Inteiro que representa univocamente um exercício.\n
#	LINK:		Caminho de arquivo para o html a ser parseado.\n
#	EXTYPE:		Tipo de exercicio a ser tratado.\n
#	EXFORMAT:	Formato do exercício a ser tratado.\n
#	ITEMS:		Lista de items.\n
class Exercise(models.Model):
	identity = models.IntegerField()
	field = models.CharField(max_length=32)
	value = models.TextField()

	def __unicode__(self):
		return u'%d : %s = %s' % (self.identity, self.field, self.value)

## Classe que define o modelo de Ids disponíveis.
#	É utilizada para cadastro de contas no banco de dados.
#
#	ID:			Pilha de inteiros que identificam locais disponíveis para 
#					inserção de contas.\n
class Identities(models.Model):
	identity = models.IntegerField()
	model = models.TextField()

	def __unicode__(self):
		return u'%d : %s' % (self.identity, self.model)

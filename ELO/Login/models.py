from django.db import models

## @package LoginModels

# Este arquivo define os modelos de Login no sistema, ou seja, os tipos de usuários que podem fazer login.
# Define como é formatada a tabela no banco de dados, de forma que cada usuário está armazenado em tabelas triple. Cada elemento da tabela
# terá um Id, um campo que armazena o nome do campo analisado e um com o valor contido dentro desse campo.

## Classe que define o modelo de estudante.
# Representa o modelo de um aluno armazenado no banco de dados.
class Student(models.Model):
	identity = models.IntegerField()
	field = models.CharField(max_length=32)
	value = models.TextField()

	## Retorna os valores do aluno correspondente ao Id no banco de dados.
	def __unicode__(self):
		return u'%s : %s = %s' % (str(self.identity), self.field, self.value)

## Classe que define o modelo de administrador.
# Representa o modelo de um administrador armazenado no banco de dados.
class Adm(models.Model):
	identity = models.IntegerField()
	field = models.CharField(max_length=32)
	value = models.TextField()

	## Retorna os valores do administrador correspondente ao Id no banco de dados.
	def __unicode__(self):
		return u'%s : %s = %s' % (str(self.identity), self.field, self.value)

## Classe que define o modelo de professor.
# Representa o modelo de um professor armazenado no banco de dados.
class Professor(models.Model):
	identity = models.IntegerField()
	field = models.CharField(max_length=32)
	value = models.TextField()

	## Retorna os valores do professor correspondente ao Id no banco de dados.
	def __unicode__(self):
		return u'%s : %s = %s' % (str(self.identity), self.field, self.value)

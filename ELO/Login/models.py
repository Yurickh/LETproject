from django.db import models

class Student(models.Model):
	identity = models.IntegerField()
	field = models.CharField(max_length=32)
	value = models.TextField()

	def __unicode__(self):
		return u'%s : %s = %s' % (str(self.identity), self.field, self.value)

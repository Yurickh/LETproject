from django.db import models

class Login(models.Model):
	user = models.IntegerField()
	field = models.CharField(max_length = 4)
	value = models.TextField()

	def __unicode__(self):
		return str(self.field) + " = " + str(self.value)

	class Meta:
		ordering = ['user']
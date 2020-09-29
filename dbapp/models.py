from django.db import models

# Create your models here.
class student(models.Model):
	sname=models.CharField(max_length=10)
	sage=models.IntegerField()

	class Meta:
		verbose_name ="student"
		verbose_name_plural ="student"

	def __str__(self):
		return '%s' %{self.sname}

   
   
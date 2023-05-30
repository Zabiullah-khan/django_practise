from django.db import models

class Student(models.Model):
	name=models.CharField(max_length=100)
	age=models.IntegerField()
	std = models.IntegerField()
	
	def __str__(self):
		if self.name==None:
			return 'error'
		return self.name

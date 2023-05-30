from django.db import models

# Create your models here.
class ModelOne(models.Model):
	name = models.CharField(max_length=30)
	standard = models.IntegerField()
	section = models.CharField(max_length=3)
	age = models.IntegerField()

from django.db import models

# Create your models here.
class Login(models.Model):
	user_email = models.CharField(max_length=60)
	user_pass = models.CharField(max_length=60)

class Signin(models.Model):
	name = models.CharField(max_length=60)
	email = models.CharField(max_length=60)
	password = models.CharField(max_length=60)
	repassword = models.CharField(max_length=60)
	

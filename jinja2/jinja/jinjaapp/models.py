from django.db import models


class FirstModel(models.Model):
	serial_id = models.IntegerField()
	stu_name = models.CharField(max_length=30,default='not available')
	stu_mail = models.EmailField(max_length=60,default='not available')
	stu_pass = models.CharField(max_length=30,default='not available')
	comment = models.CharField(max_length = 40, default='not available')
	
	

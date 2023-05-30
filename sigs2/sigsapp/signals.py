from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save

@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
	print(sender)
	print(request)
	print(user)
	print(f'{kwargs}')

@receiver(pre_save,sender=User)
def  beforesave(sender,instance,**kwargs):
	print('pre save running')

@receiver(post_save,sender=User)
def aftersave(sender,instance,created,**kwargs):
	if created:
		print('new record')
	else:
		print('updating existed record')

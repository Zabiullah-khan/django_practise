from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User


@receiver(sender=User)
def log_sig(sender,request,user,**kwargs):
	print('signal sent...')
	print(sender)
	print(request)
	print(user)
	print(f'{kwargs}')



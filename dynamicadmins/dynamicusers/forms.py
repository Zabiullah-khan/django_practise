from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserChangeForm

class UserEditForm(UserChangeForm):
	password = None
	class Meta:
		model = User
		fields=['username','first_name','last_name','email']
		

from django import forms
from .models import Login,Signin
from django.core import validators
import re

pattern = re.compile('[_.,?><:;~!@#$%^&*)(]')
def checkpoint(name):
	check = pattern.search(name)
	
	if len(name)<5:
		raise forms.ValidationError('Name Should Contain more than Four Characters')
	elif check != None:
		raise forms.ValidationError('Name Should not Contain any Special Characters')

def check_pass (password):
	
	chk_pas = pattern.search(password)
	if len(password)<6 :
		raise forms.ValidationError('Password should not be less than Six Characters')
	elif chk_pas == None :
		raise forms.ValidationError('Password Must Contain atleast One Special Character')
		
class LoginModel(forms.ModelForm):
	class Meta:
		model = Login
		fields=['user_email','user_pass']

class SignModel(forms.ModelForm):
	name=forms.CharField(validators=[checkpoint],widget=forms.TextInput())
	password = forms.CharField(validators=[check_pass],widget=forms.PasswordInput())
	
	class Meta :
		model = Signin
		fields=['name','email','password','repassword']
		error_messages={
		'name':{'required':'This Field Should Not Be Empty'}
		}
		
		widgets= {
			'repassword':forms.PasswordInput()
		}
		
	def clean(self):
		
		paz = self.cleaned_data.get('password')
		repaz = self.cleaned_data.get('repassword')
		if paz != repaz :
			raise forms.ValidationError('Password Doesnt Match')

	
	
		
		

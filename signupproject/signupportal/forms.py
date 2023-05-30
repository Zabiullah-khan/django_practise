from django import forms
from django.core import validators
from signupportal.models import SignModel
import re

spchr= re.compile('[~`!@#$%^&*)(_]')
def checkpoint(name):

	cksp = spchr.search(name)
	if len(name)<6:
		raise forms.ValidationError('Name Should Not Be Lesser Than Six Characters')
	elif cksp != None :
		raise forms.ValidationError('Name Should Not COntainANy Special Character ')

def passchk(password):
	ckpw=spchr.search(password)
	if len(password) < 6 :
		raise forms.ValidationError('Password Must Be Minimum Six Characters Long')
	elif  ckpw == None :
	 	raise forms.ValidationError('Password Must Contain Atleast One Special Character')
		
class SignupForm(forms.ModelForm):
	name = forms.CharField(validators=[checkpoint],max_length=60,widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(validators=[passchk],max_length=60,widget=forms.PasswordInput(attrs={'class':'form-control'}))
	repassword = forms.CharField(max_length=60,widget=forms.PasswordInput(attrs={'class':'form-control'}))
	class Meta:
		model = SignModel
		fields =['name','email','password','repassword']
		error_messages = {
			
			'name' : {'required':'Name Field Should Not Be Empty'},
			'password':{'required':'Password Field Should Not Be Empty'},
			'repasswrod':{'required':'Password Field Should Not Be Empty'},
		
		}
		
		widgets= {
			
			'email':forms.EmailInput(attrs={'class':'form-control'})
		
		}
	
	def clean(self):
		
		cleaned_data = super().clean()
		paz = self.cleaned_data.get('password')
		repaz = self.cleaned_data.get('repassword')
		if paz != repaz :
			raise forms.ValidationError('Password Doesnt Match')

class  LoginForm(forms.Form):
	user_email = forms.CharField(max_length=60,widget=forms.EmailInput(attrs={'class':'form-control'}))
	user_password = forms.CharField(max_length=60,widget=forms.PasswordInput(attrs={'class':'form-control'}))	
		
		

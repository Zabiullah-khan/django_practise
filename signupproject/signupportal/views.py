from django.shortcuts import render
from django.http import HttpResponseRedirect
from signupportal.forms import SignupForm,LoginForm
from signupportal.models import SignModel
# Create your views here.

def signform(request):
	
	if request.method=='POST':
		fm = SignupForm(request.POST)
		if fm.is_valid():
			namz = fm.cleaned_data.get('name')
			emailz = fm.cleaned_data.get('email')
			passwordz = fm.cleaned_data.get('password')
			
			pointer = SignModel(name=namz,email=emailz,password=passwordz)
			pointer.save()
			
			return HttpResponseRedirect('/')
	else:
		fm=SignupForm()
		lm=LoginForm()

	return render(request,'signupform.html',{'frm':fm,'lrm':lm})

from django.shortcuts import render
from django.http import HttpResponseRedirect
from authapp.forms import LoginModel,SignModel
from datetime import datetime
from authapp.models import Signin

# Create your views here.
def loginpagan(request):
	
	form_template =LoginModel()
	return render(request,'authapp/templates/loginform.html',{'frm':form_template})

def signpagan(request):
	dts = datetime.now()	
	if request.method == 'POST':
		data = SignModel(request.POST)
		if data.is_valid() :
			namz = data.cleaned_data.get('name')
			emailz = data.cleaned_data.get('email')
			pazz = data.cleaned_data.get('password')
			
			pointer = Signin(name=namz,email=emailz,password=pazz)
			pointer.save()
			return HttpResponseRedirect('/')			
		
	else :
		data = SignModel()
	return render(request,'authapp/templates/signform.html',{'sgn':data})

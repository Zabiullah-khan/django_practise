from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages

# Create your views here.
def log(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			fm = AuthenticationForm(request=request,data=request.POST)
			if fm.is_valid():
				unam = fm.cleaned_data.get('username')
				upass = fm.cleaned_data.get('password')
				user = authenticate(username=unam,password=upass)
				if user is not None:
					login(request,user)
					return HttpResponseRedirect('/login/dash')
				else :
					
					return HttpResponseRedirect('/login/login')
				
		else:
			fm = AuthenticationForm()
		return render(request,'loginpage.html',{'frm':fm})
	else:
		return HttpResponseRedirect('/login/dash')
	
def  dash(request):
	if request.user.is_authenticated:
		messages.info(request,'Login Success')
		return render(request,'dashbrd.html')
	else:
		return HttpResponseRedirect('/login/login')
def logoutz(request):
	logout(request)
	return HttpResponseRedirect('/login/login')

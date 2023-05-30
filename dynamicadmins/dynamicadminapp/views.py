from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
	if request.method == 'POST':
		fm = SignUpForm(request.POST)
		if fm.is_valid():
			fm.save()
			messages.success(request,'Account Registered Succesfully')
	
	else:
		fm = SignUpForm()
	return render(request,'home.html',{'frm':fm})

def loginform(request):
	if  not request.user.is_authenticated:
	
		if request.method=='POST':
			
			fm = AuthenticationForm(request=request,data=request.POST)
			if fm.is_valid():
				uname = fm.cleaned_data.get('username')
				upass = fm.cleaned_data.get('password')

				user = authenticate(username=uname,password=upass)
				
				if user is not None:
					login(request,user)
					return HttpResponseRedirect('/profile/profiles/')
					
				
		else:
			fm=AuthenticationForm()
		return render(request,'loginpage.html',{'frm':fm})
	else:
		return HttpResponseRedirect('/profile/profiles/')

def log_out(request): 
	logout(request)
	return HttpResponseRedirect('/login/login')

def password_change(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			fm = PasswordChangeForm(user=request.user,data=request.POST)
			if fm.is_valid():
				fm.save()
				update_session_auth_hash(request,fm.user)
				return HttpResponseRedirect('/login/login')	
		else:
			fm = PasswordChangeForm(user=request.user)
		return render(request,'passwordchange.html',{"frm":fm})
	else:
		return HttpResponseRedirect('/login/login')		

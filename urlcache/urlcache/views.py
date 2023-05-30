from django.shortcuts import render

def home(request):
	request.session['uname']='jam'
	return render(request,'home.html')

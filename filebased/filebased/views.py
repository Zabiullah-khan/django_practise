from django.shortcuts import render,HttpResponse

def home(request):
	request.session['name']='khan'
	return render(request,'home.html')

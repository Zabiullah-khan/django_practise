from django.shortcuts import render,HttpResponse

def home(request):
	request.session['name'] = 'PageCounter'
	return render(request,'home.html')

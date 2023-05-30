from django.shortcuts import render

def home(request):
	request.session['name']='zabi'
	return render(request,'home.html')

	

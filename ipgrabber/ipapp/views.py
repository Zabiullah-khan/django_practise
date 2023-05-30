from django.shortcuts import render

# Create your views here.
def home(request):
	ip = request.META.get('REMOTE_ADDR')
	return render(request,'home.html',{'ip':ip})

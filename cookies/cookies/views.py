from django.shortcuts import render,HttpResponseRedirect
from datetime import datetime,timedelta

def setcookies(request):
	msg=''
	response=render(request,'setcookies.html',{'msg':msg})
	st=response.set_signed_cookie('name','zabi',salt='nm')
	if st:
		msg='Cookies Set....'
	else:
		msg = 'Cookies Not Set....'
	return response

def getcookies(request):
	name = request.get_signed_cookie('name','Guest',salt='nm')
	return render(request,'getcookies.html',{'nam':name})

def delcookies(request):
	response=render(request,'deletecookies.html')
	response.delete_cookie('name')
	return response
	

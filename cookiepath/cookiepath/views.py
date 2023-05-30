from django.shortcuts import render,HttpResponse

def setsession(request):
	request.session.set_test_cookie()	
	bol=request.session.test_cookie_worked()
	if bol:
		request.session.delete_test_cookie()
		request.session['name']='zabi'
		return render(request,'setsession.html')
	else:
		return HttpResponse('Kindly Enable Your Cookies')

def getsession(request):
	ss=request.session.get('name','Guest')
	return render(request,'getsession.html',{'ss':ss})
	

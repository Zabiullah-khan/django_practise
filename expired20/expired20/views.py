from django.shortcuts import render,HttpResponse

#set_cookies
def setsession(request):
	bol=request.session.set_test_cookie()
	sol = request.session.test_cookie_worked()
	print(sol)
	if  sol:
		request.session['name']='zabi'
		return render(request,'setsession.html')
	else:
		return HttpResponse('Cookies Could not be set')
		
#get_cookies
def getsession(request):
	if 'name' in request.session:
		ss = request.session.get('name','Guest')
		request.session.modified = True
		return render(request,'getsession.html',{'ss':ss})
	else:
		return HttpResponse('cookies session ended')

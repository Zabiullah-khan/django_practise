from django.shortcuts import render,HttpResponseRedirect

def home(request):
	if request.method=='POST':
		unum = request.POST.get('acname')
		request.session['acname']=unum
		print(unum,'cookies set')
		return HttpResponseRedirect('/get/')
	return render(request,'home.html')

def getsession(request):
	gotac=request.session.get('acname')
	return render(request,'getcookies.html',{'got':gotac})

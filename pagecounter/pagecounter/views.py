from django.shortcuts import render,HttpResponse

def home(request):
	cnt = request.session.get('count',0)
	counter = cnt + 1
	cset=request.session['count']=counter
	return render(request,'pagecounter.html',{'c':cset})

from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from jinjaapp.models import FirstModel
def  home(request):
	
	d = datetime.now()
	
	dics = {}
	
	obj = FirstModel.objects.all()
	
	try:
	
		if request.method == 'GET' :
			stu_i = request.GET.get('idd')
			stu_n = request.GET.get('nam')
			stu_e = request.GET.get('emai')
			stu_p = request.GET.get('pas')
			stu_c = request.GET.get('com')
			x = FirstModel(serial_id=stu_i,stu_name=stu_n,stu_mail=stu_e,stu_pass=stu_p,comment=stu_c)
			x.save()
			
			print('executed')
			return render(request,'jinhae.html',{'stu':obj})
	except Exception as e:
		print(e)
		print('exception error')
		
	return render(request,'jinhae.html',{'stu':obj})
from django.shortcuts import render
from django.http import HttpResponse
from todoapp.models import TodoFields
def home(request):
	
	get_data = TodoFields.objects.all()
	data = {
		'data_fetch' : get_data,
	}
	
	try:
		if request.method == 'GET':
			dele_val = request.GET.get('vals')
			print(dele_val)
			get_del= TodoFields.objects.get(pk=dele_val)
			get_del.delete()
			return render(request,'index.html',data)
	except Exception as e :
		print(e)
	
	return render(request,'index.html',data)
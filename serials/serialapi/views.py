from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

def routeapi(request,pk):
	get_instance=Student.objects.get(pk=pk)
	sear=StudentSerializer(get_instance)
	content=JSONRenderer().render(sear.data)
	return HttpResponse(content)

		

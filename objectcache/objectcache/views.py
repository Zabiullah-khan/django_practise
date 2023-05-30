from django.shortcuts import render
from django.core.cache import cache
def home(request):
	vr = cache.get_or_set('name','zabiullah',20,version=1)
	return render(request,'home.html',{'vr':vr})

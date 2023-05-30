from django.shortcuts import render
from django.http import HttpResponseRedirect
from dynamicusers.forms import UserEditForm
from django.contrib import messages
# Create your views here.
def profilez(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			fm = UserEditForm( request.POST,instance=request.user)
			if fm.is_valid():
				fm.save()
				messages.info(request,'Saved Successfully')
		else:
			fm=UserEditForm(instance=request.user)
		return render(request,'dynamicusers/templates/profile.html',{'frm':fm})
	else:
		return HttpResponseRedirect('/login/login')

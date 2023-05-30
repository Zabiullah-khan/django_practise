from django.contrib import admin
from .models import Signin
# Register your models here.

class SignAdmin(admin.ModelAdmin):
	list_display = ['name','email','password']
	

admin.site.register(Signin , SignAdmin)

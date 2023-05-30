from django.contrib import admin
from signupportal.models import SignModel
# Register your models here.

class SignAdmin(admin.ModelAdmin):
	list_display =['name','email','password']
	
	
admin.site.register(SignModel,SignAdmin)

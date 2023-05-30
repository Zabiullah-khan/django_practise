from django.contrib import admin
from todoapp.models import TodoFields
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
	list_display = ('id','dtime','summary')

admin.site.register(TodoFields,TodoAdmin)
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	class Meta:
		model = Student
		fields = '__all__'
		

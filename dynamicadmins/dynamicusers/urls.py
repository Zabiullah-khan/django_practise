from django.urls import path
from dynamicusers import views
urlpatterns=[
	path('profiles/',views.profilez,name='profiles'),
]

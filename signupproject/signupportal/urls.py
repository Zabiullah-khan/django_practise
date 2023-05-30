from django.urls import path
from signupportal import views

urlpatterns = [

	path('signup/',views.signform,name='signup')
]

from django.urls import path
from ipapp import views
urlpatterns =[
	path('home',views.home,name='home')
]

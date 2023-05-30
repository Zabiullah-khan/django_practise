from django.urls import path
from . import views
urlpatterns=[
	path('apikey/<int:pk>/',views.routeapi,name='apikey')
]

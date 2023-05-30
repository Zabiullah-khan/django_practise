from django.urls import path
from visitingtemplate import views
urlpatterns= [
	path('card',views.cardhome,name='card')
]
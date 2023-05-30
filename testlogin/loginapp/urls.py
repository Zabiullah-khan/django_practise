from django.urls import path
from loginapp import views

urlpatterns =[

	path('login',views.log,name='login'),
	path('dash',views.dash,name='dash'),
	path('logouz',views.logoutz,name='logouz')
]

from django.urls import path
from dynamicadminapp import views

urlpatterns=[

	path('home',views.home,name='home'),
	path('login',views.loginform,name='login'),
	path('logout/',views.log_out,name='logout'),
	path('pcg/',views.password_change,name='passchange'),
]

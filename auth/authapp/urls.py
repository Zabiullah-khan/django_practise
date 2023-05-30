from django.urls import path
from authapp import views
urlpatterns=[
	
	path('logfrm/',views.loginpagan,name='logfrm'),
	path('signfrm/',views.signpagan,name='signfrm'),

]

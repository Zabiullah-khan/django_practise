from django.apps import AppConfig


class SigsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sigsapp'
    
    def ready(self):
    	import sigsapp.signals

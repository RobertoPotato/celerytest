from django.apps import AppConfig


class InputConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Input'

    def ready(self):
    	from jobs import updater
    	updater.start()

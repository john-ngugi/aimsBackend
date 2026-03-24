# landuse/apps.py
from django.apps import AppConfig


class LandUseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'landuse'

    def ready(self):
        import landuse.signals
        print("Signals loaded!")  # add this to confirm it runs on startup
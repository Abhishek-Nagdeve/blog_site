from django.apps import AppConfig


class UsrsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usrs'

    def ready(self):
        import usrs.signals


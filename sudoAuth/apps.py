from django.apps import AppConfig


class SudoauthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sudoAuth'


    def ready(self):
        import sudoAuth.signals


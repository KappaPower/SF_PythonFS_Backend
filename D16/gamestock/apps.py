from django.apps import AppConfig


class GameStockConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gamestock'

    def ready(self):
        # pass
        import gamestock.signals

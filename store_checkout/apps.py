from django.apps import AppConfig


class StoreCheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store_checkout'

    def ready(self):
        import store_checkout.signals

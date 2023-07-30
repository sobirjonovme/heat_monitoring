from django.apps import AppConfig


class ChickenFarmConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.chicken_farm"

    def ready(self):
        import apps.chicken_farm.signals  # noqa

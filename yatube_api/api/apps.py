from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Класс конфигурации приложения API."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

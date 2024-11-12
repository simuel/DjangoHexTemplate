from django.apps import AppConfig


class {{ app_name|capfirst }}Config(AppConfig):
    name = 'apps.{{app_name}}'

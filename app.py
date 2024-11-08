from django.apps import AppConfig


class {{ app_name|capfirst }}Config(AppConfig):
    name = 'Apps.{{app_name}}'

from django.apps import AppConfig
from .signals import build_settings
from django.db.models.signals import post_migrate


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project.apps.core'
    label = 'core'

    def ready(self) -> None:
        post_migrate.connect(build_settings, sender=self)

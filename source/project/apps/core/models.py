from django.db import models
from django.contrib.sites.models import Site

# Create your models here.


class Settings(Site):

    class Meta:
        verbose_name_plural = 'settings'
        db_table = 'core_settings'

    def __str__(self) -> str:
        return 'Settings'

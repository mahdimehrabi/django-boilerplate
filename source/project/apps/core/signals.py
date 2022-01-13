from django.dispatch import receiver


def build_settings(sender, **kwargs):
    from django.contrib.sites.models import Site
    from .models import Settings
    if Settings.objects.count() < 1:
        Settings.objects.create(site_ptr=Site.objects.first())

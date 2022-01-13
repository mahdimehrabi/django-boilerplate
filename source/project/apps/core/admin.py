from django.contrib import admin
from . import models
from django.contrib.sites.models import Site
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)


admin.site.unregister(Site)


@admin.register(models.Settings)
class SettingAdminModel(admin.ModelAdmin):
    def has_add_permission(self, request) -> bool:
        return False

    def has_delete_permission(self, request, object=None) -> bool:
        return False

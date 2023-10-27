from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Profile


# Register your models here.
class ProfileAdmin(ModelAdmin):
    list_display = ("email", "last_name", "first_name", "bio", "picture", "user", "id")


admin.site.register(Profile, ProfileAdmin)

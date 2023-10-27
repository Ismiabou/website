from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Maison, Poster

# Register your models here.
class MaisonAdmin(ModelAdmin):
    list_display = ('stat', 'description', 'prix_loc', 'prix_achat', 'image')

admin.site.register(Maison, MaisonAdmin)
admin.site.register(Poster)
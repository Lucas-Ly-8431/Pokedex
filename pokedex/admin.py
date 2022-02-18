from django.contrib import admin

from pokedex.models import Pokemon, Type

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Type)
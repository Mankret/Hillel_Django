from django.contrib import admin

from .models import Country, Developer, Game, Genre

admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(Developer)
admin.site.register(Country)

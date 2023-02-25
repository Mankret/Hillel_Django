from celery_beat_parsing.models import Author, Quotes

from django.contrib import admin


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Quotes)
class QuotesAdmin(admin.ModelAdmin):
    list_display = ['quote', 'author']
    list_filter = ['author']
    search_fields = ['author']

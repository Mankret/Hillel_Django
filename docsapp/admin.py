from django.contrib import admin

from docsapp.models import Author, Book, Publisher, Store


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    list_filter = ['name', 'age']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'rating', 'pubdate']
    list_per_page = 10
    list_select_related = ['publisher']
    raw_id_fields = ['authors']

    list_filter = ['pubdate']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name']
    raw_id_fields = ['books']
    list_filter = ['name']

from django.contrib import admin

from mathapp.models import LogModel, Person

admin.site.register(Person)


@admin.register(LogModel)
class LogModelAdmin(admin.ModelAdmin):
    list_display = ('path', 'method', 'created')
    fieldsets = [
        ('Information', {'fields': ['path']}),
        ('Detail', {'fields': ['method', 'body', 'query', 'user'], 'classes': ('wide', 'extrapretty')})
    ]

    list_filter = ['created', 'method', 'user']
    search_fields = ['path']
    date_hierarchy = 'created'

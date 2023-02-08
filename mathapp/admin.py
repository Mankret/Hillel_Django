from django.contrib import admin

from mathapp.models import Person, LogModel

admin.site.register(Person)


@admin.register(LogModel)
class LogModelAdmin(admin.ModelAdmin):
    list_display = ('path', 'method', 'create')
    fieldsets = [
        ('Information', {'fields': ['path']}),
        ('Detail', {'fields': ['method', 'body', 'query', 'user'], 'classes': ('wide', 'extrapretty')})
    ]

    list_filter = ['create', 'method', 'user']
    search_fields = ['path']
    date_hierarchy = 'create'

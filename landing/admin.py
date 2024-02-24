from django.contrib import admin
from .models import Project, Contact

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'priority')
    ordering = ('-priority',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    readonly_fields = ('created_at',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact, ContactAdmin)

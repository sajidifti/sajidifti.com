from django.contrib import admin
from .models import Project, Contact

# Register your models here.




class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    readonly_fields = ('created_at',)


admin.site.register(Project)
admin.site.register(Contact, ContactAdmin)

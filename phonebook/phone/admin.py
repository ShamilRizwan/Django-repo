from django.contrib import admin
from .models import Contacts
# Register your models here.

class ContactsAdmin(admin.ModelAdmin):
    list_display=('name','number')
    ordering=('name',)
    search_fields=('name','number')
admin.site.register(Contacts,ContactsAdmin)
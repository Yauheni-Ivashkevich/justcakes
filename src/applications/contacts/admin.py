from django.contrib import admin
from django.contrib.admin import ModelAdmin

from applications.contacts.models import Contact

@admin.register(Contact)
class ContactAdminModel(ModelAdmin):
    pass

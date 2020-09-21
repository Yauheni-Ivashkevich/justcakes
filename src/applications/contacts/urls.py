from django.urls import path
from applications.contacts.apps import ContactsConfig
from applications.contacts.views import ContactsView

app_name = ContactsConfig.name

urlpatterns = [
    path("", ContactsView.as_view(), name="contacts_index"),
]

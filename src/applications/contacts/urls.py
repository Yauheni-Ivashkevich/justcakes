from django.urls import path
from applications.contacts.apps import IndexConfig
from . import views

app_name = IndexConfig.name

urlpatterns = [
    path("contacts", views.ContactsView.as_view(), name="contacts_index"),
]

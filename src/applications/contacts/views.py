from django.shortcuts import render
from django.views.generic import View


from applications.contacts.models import Contact


class ContactsView(View):
    """Список контактов"""
    def get(self, request):
        contacts = Contact.objects.all()
        return render(request, 'contacts/contacts_index.html', {"contacts_index": contacts})


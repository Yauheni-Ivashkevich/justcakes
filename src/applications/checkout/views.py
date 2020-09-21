from django.shortcuts import render
from django.views.generic import View


from applications.checkout.models import CheckoutInfo


class CheckoutView(View):
    """Оплата"""
    def get(self, request):
        information = CheckoutInfo.objects.all()

        return render(request, 'checkout/checkout_index.html', {"information": information})


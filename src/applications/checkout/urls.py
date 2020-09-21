from django.urls import path

from applications.checkout.apps import CheckoutConfig
from applications.checkout.views import CheckoutView

app_name = CheckoutConfig.name

urlpatterns = [
    path("", CheckoutView.as_view(), name="checkout"),
]

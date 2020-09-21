from django.contrib import admin
from django.contrib.admin import ModelAdmin

from applications.checkout.models import CheckoutInfoOption
from applications.checkout.models import CheckoutInfo


@admin.register(CheckoutInfo)
class CheckoutInfoAdminModel(ModelAdmin):
    pass

@admin.register(CheckoutInfoOption)
class CheckoutInfoOptionAdminModel(ModelAdmin):
    pass

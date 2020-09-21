from django.contrib import admin
from django.contrib.admin import ModelAdmin

from applications.index.models import Cake
from applications.index.models import Cake_name
from applications.index.models import Reviews


@admin.register(Cake)
class CakeAdminModel(ModelAdmin):
    pass


@admin.register(Cake_name)
class Cake_nameAdminModel(ModelAdmin):
    pass


@admin.register(Reviews)
class ReviewsAdminModel(ModelAdmin):
    pass


# admin.site.register(Cake)
# admin.site.register(Cake_name)
# admin.site.register(Reviews)

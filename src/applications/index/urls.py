from django.urls import path

from applications.index.apps import IndexConfig
from applications.index.views import CakesView
from applications.index.views import CakeDetailView

app_name = IndexConfig.name

urlpatterns = [
    path("", CakesView.as_view(), name="cake_index"),
    path("<url>/<int:pk>", CakeDetailView.as_view(), name="cake_detail"),
]

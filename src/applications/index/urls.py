from django.urls import path

from applications.index.views import CakesView
from applications.index.views import CakeDetailView


urlpatterns = [
    path("", CakesView.as_view(), name="cake_index"),
    path("<url>/<int:pk>", CakeDetailView.as_view(), name="cake_detail"),
    # path("", views.CakesView.as_view, name="contacts"),
]

#
# from django.urls import path
#
# from applications.contacts.apps import IndexConfig
# from applications.contacts.views import IndexView
#
# app_name = IndexConfig.name
#
# urlpatterns = [
#     path("", IndexView.as_view(), name="contacts"),
# ]

from django.urls import path

from . import views


urlpatterns = [
    path("", views.CakesView.as_view(), name="cake_index"),
    path("<int:pk>/", views.CakeDetailView.as_view(), name="cake_detail"),
    # path("", views.CakesView.as_view, name="index"),
]

#
# from django.urls import path
#
# from applications.index.apps import IndexConfig
# from applications.index.views import IndexView
#
# app_name = IndexConfig.name
#
# urlpatterns = [
#     path("", IndexView.as_view(), name="index"),
# ]

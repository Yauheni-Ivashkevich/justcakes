from django.shortcuts import render
from django.views.generic import View

from applications.index.models import Cake


class CakesView(View):
    """Список видов десертов"""

    def get(self, request):
        cakes = Cake.objects.all()
        return render(request, "index/cake_index.html", {"cake_index": cakes})


class CakeDetailView(View):
    """Полное описание десерта"""

    def get(self, request, url, pk):
        cake = Cake.objects.get(id=pk)

        return render(request, "index/cake_detail.html", {"cake": cake})

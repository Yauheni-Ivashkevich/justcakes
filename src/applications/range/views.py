# from django.shortcuts import render
# from range.models import Cake
#
#
# def cake_index(request):
#     cakes = Cake.objects.all()
#     context = {"cakes": cakes}
#     return render(request, "cake_index.html", context)
#
#
# def cake_detail(request, pk):
#     cake = Cake.objects.get(pk=pk)
#     context = {"cake": cake}
#     return render(request, "cake_detail.html", context)# первоначальная задумка

"""from django.views.generic import ListView 

from applications.range.models import Cake


class RangeView(ListView):
    template_name = "range/cake_detail.html"
    model = Cake

    def get_context_data(self, **kwargs):
        context = super(RangeView, self).get_context_data(**kwargs)
        context["cake_list"] = Cake.objects.all()
        return context""" # попытка решения через ListView
from django.shortcuts import render
from django.views.generic import View


from applications.index.models import Cake


class CakesView(View):
    """Список видов десертов"""
    def get(self, request):
        cakes = Cake.objects.all()
        return render(request, 'index/cake_index.html', {"cake_index": cakes})


class CakeDetailView(View):
    """Полное описание десерта"""
    def get(self, request, url, pk):
        cake = Cake.objects.get(id=pk)

        return render(request, 'index/cake_detail.html', {
            'cake': cake
        })




#     template_name = "contacts/contacts_index.html"
#

# from django.shortcuts import render
#
#
# def contacts(request):
#     return render(request, 'contacts/contacts_index.html', {
#         'body_message':
#             ['Cakes', 'Cupcakes', 'Gingers'],
#     })
#
#
# from django.views.generic import TemplateView
#
# from applications.contacts.models import Cake
#
#
# class IndexView(TemplateView):
#     template_name = "contacts/contacts_index.html"
#
#     def get_context_data(self, **kwargs):
#         parent_ctx = super().get_context_data(**kwargs)
#
#         info = Cake.objects.first()
#         ctx = {
#             "title": info.title,
#             "description": info.description,
#             "ingredients": info.ingredients,
#             "image": info.image,
#         }
#
#         ctx.update(parent_ctx)
#
#         return ctx

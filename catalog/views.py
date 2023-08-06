
from django.views.generic import ListView, DetailView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Skystore',
    }


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': 'Skystore',
    }


class ContactListView(ListView):
    model = Product
    extra_context = {
        'title': 'Skystore',
    }
    template_name = 'catalog/contacts.html'


# def contacts(request):
#     context = {
#         'title': 'Skystore'
#
#     }
#
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#
#         print(f'\nuser: {name} \nphone: {phone} \nsend message: {message}\n')
#
#     return render(request, "catalog/contacts.html", context)

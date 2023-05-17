from django.shortcuts import render

# Create your views here.
from catalog.models import Product


def home(request):
    context = {
        'title': 'Skystore',
        'product_list': Product.objects.all()
    }
    return render(request, "catalog/home.html", context)


def product(request, pk):
    product_card = Product.objects.get(pk=pk)
    context = {
        'title': 'Skystore',
        'product': product_card
    }
    return render(request, "catalog/product_card.html", context)


def contacts(request):
    context = {
        'title': 'Skystore'

    }

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f'\nuser: {name} \nphone: {phone} \nsend message: {message}\n')

    return render(request, "catalog/contacts.html", context)

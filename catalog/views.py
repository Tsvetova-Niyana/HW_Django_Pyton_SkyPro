from django.shortcuts import render


# Create your views here.
from catalog.models import Product


def home(request):
    context = {
        'title': 'Skystore',
        'product_list': Product.objects.all()
    }
    return render(request, "catalog/home.html", context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f'\nuser: {name} \nphone: {phone} \nsend message: {message}\n')

    return render(request, "catalog/contacts.html")

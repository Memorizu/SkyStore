from django.shortcuts import render
from catalog.models import Product, Contact


def index(request):
    latest_five_products = Product.objects.order_by('create_date')[:5]

    for product in latest_five_products:
        print(f'Продукт: {product}')

    return render(request, 'catalog/index.html')


def contacts(request):
    contact = Contact.objects.get(country='Россия')
    if request.method == 'POST':
        print(request.POST.get('name'))
        print(request.POST.get('phone'))
        print(request.POST.get('message'))
    return render(request, 'catalog/contacts.html', {'contact': contact})

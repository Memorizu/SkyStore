from django.shortcuts import render
from catalog.models import Product, Contact, Category


def index(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории'
    }

    return render(request, 'catalog/index.html', context)


def contacts(request):
    contact = Contact.objects.get(country='Россия')
    if request.method == 'POST':
        print(request.POST.get('name'))
        print(request.POST.get('phone'))
        print(request.POST.get('message'))
    return render(request, 'catalog/contacts.html', {'contact': contact})


def product(request, pk: int):
    category = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Продукты категории {category}'
    }
    return render(request, 'catalog/product.html', context)


def all_product(request):

    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/products.html', context)


from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from catalog.models import Product, Category, Contact


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории'
    }


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Продукты'
    }





class ProductByCategoryListView(ListView):
    model = Product
    template_name = 'catalog/product.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_id'] = category_item
        context_data['title'] = f'Продукты категории {category_item.name}'
        return context_data

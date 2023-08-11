from typing import Any, Dict
from django.forms import inlineformset_factory
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from product.models import Product
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.urls import reverse, reverse_lazy
from catalog.models import Category
from product.forms import ProductForm
from version.forms import VersionForm
from version.models import Version


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Продукты'
    }

class ProductDetailView(DetailView):
    model = Product
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))
        return queryset
    
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:category')
    
    
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:category')
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        
        if self.request.method == 'POST':
            formset = VersionFormSet(self.request.POST, instance=self.object)
        else:
            formset = VersionFormSet(instance=self.object)
        context_data['formset'] = formset   
        
        return context_data
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        context_data = self.get_context_data()       
        formset = context_data['formset']
        self.object = form.save()
        
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)
    
    
class ProductByCategoryListView(ListView):
    model = Product

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


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:category')
    
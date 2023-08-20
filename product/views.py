from typing import Any, Dict, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.forms import inlineformset_factory
from django.forms.models import BaseModelForm
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from product.models import Product
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.urls import reverse, reverse_lazy
from product.forms import ProductForm
from version.forms import VersionForm
from version.models import Version
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    extra_context = {
        'title': 'Продукты'
    }
    
    def get_queryset(self):
        queryset = super().get_queryset()   
        category_id = self.kwargs.get('pk')
        queryset = Product.objects.filter(category_id=category_id)
        return queryset
    
    

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
   
     
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:category')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:category')
    
    permission_required = 'product.can_change_desc_permission'
    
    def has_permission(self):
        obj = self.get_object()
        if self.request.user == obj.user or self.request.user.is_staff:
            return True
        return super().has_permission()
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        
        if self.request.method == 'POST':
            formset = VersionFormSet(self.request.POST, instance=self.object)
        else:
            formset = VersionFormSet(instance=self.object)
        context_data['formset'] = formset   
        
        return context_data
    
    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        user = self.request.user
        obj = self.get_object()

        if user.has_perm('product.can_change_desc_permission') and user != obj.user:
            form.instance.description = obj.description
            
        if user.has_perm('product.can_change_category_permission') and user != obj.user:
            form.instance.category = obj.category

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
            
        return super().form_valid(form)
    

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:category')
    
    
class ProductUserLIstView(LoginRequiredMixin, ListView):
    model = Product
    
    def get_queryset(self):
        queryset =  super().get_queryset()
        user = self.request.user
        queryset = Product.objects.filter(user_id=user.id)
        return queryset

from django.urls import reverse_lazy
from django.views.generic import ListView

from catalog.models import Category


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории'
    }

from django.views.generic import ListView 
from catalog.services import get_cached_category
from catalog.models import Category
from django.conf import settings

class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории'
    }

    def get_queryset(self):
        if settings.CACHE_ENABLED:
            category_list = get_cached_category()
            return category_list
        return super().get_queryset()
        
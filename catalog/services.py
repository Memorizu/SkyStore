from django.core.cache import cache
from catalog.models import Category


def get_cached_category():

    key = 'category_list'
    category_list = cache.get(key)
        
    if category_list is None:
        category_list = Category.objects.all()
        cache.set(key, category_list, 60 * 15)    
    return category_list
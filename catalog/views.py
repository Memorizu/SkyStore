from django.urls import reverse_lazy
from django.views.generic import ListView #DetailView

from catalog.models import Category
from product.models import Product

class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории'
    }

# class CategoryDetailView(DetailView):
#     model = Category
    
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         category_id = self.kwargs.get('pk')
#         queryset = Product.objects.filter(category_id=category_id)
#         print(queryset)
#         return queryset

#     def get_context_data(self, *args, **kwargs):
#         context_data = super().get_context_data(*args, **kwargs)
        
#         category = self.get_object()
#         print(category)
#         product_list = self.get_queryset() 
#         print(product_list)
        
#         context_data['product_list'] = product_list
#         context_data['title'] = f'Продукты категории {category.name}'
#         return context_data

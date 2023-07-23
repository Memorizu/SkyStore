from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, all_product, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', index),
    path('contacts/', contacts, name='contacts'),
    path('products/', all_product, name='all_product'),
    path('<int:pk>/product/', product, name='product'),
]

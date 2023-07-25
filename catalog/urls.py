from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, ContactCreateView, ProductListView, ProductByCategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='category'),
    path('contacts/', ContactCreateView.as_view(), name='contacts'),
    path('product/', ProductListView.as_view(), name='product'),
    path('<int:pk>/product/', ProductByCategoryListView.as_view(), name='product'),
]

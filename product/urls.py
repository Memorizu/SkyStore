from product.views import ProductCreateView, ProductListView, ProductUpdateView, ProductDetailView, ProductDeleteView, ProductUserLIstView
from django.urls import path
from product.apps import ProductConfig
from django.views.decorators.cache import cache_page, never_cache


app_name = ProductConfig.name


urlpatterns = [
    path('<int:pk>', ProductListView.as_view(), name='products'),
    path('detail/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='detail'),
    path('create', never_cache(ProductCreateView.as_view()), name='create'),
    path('update/<int:pk>', never_cache(ProductUpdateView.as_view()), name='update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
    path('my_products/', ProductUserLIstView.as_view(), name='my_products'),
]

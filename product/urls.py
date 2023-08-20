from product.views import ProductCreateView, ProductListView, ProductUpdateView, ProductDetailView, ProductDeleteView, ProductUserLIstView
from django.urls import path
from product.apps import ProductConfig


app_name = ProductConfig.name


urlpatterns = [
    path('<int:pk>', ProductListView.as_view(), name='products'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='detail'),
    path('create', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
    path('my_products/', ProductUserLIstView.as_view(), name='my_products'),
]

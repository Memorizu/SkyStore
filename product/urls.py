from product.views import ProductByCategoryListView, ProductCreateView, ProductListView, ProductUpdateView, ProductDetailView, ProductDeleteView
from django.urls import path
from product.apps import ProductConfig


app_name = ProductConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('<int:pk>/', ProductByCategoryListView.as_view(), name='product'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='detail'),
    path('create', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete')
]

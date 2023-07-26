from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name='detail'),
#     path('<int:pk>/product/', ProductByCategoryListView.as_view(), name='product'),
]

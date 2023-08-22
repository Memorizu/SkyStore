from django.urls import path
from django.views.decorators.cache import never_cache
from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('create/', never_cache(BlogCreateView.as_view()), name='create'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', never_cache(BlogUpdateView.as_view()), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
]

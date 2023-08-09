from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='category'),
]

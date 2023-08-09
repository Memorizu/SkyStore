from django.contrib import admin
from product.models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'description',)
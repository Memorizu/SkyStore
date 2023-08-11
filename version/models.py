from django.db import models
from django.urls import reverse

from product.models import Product


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.IntegerField(verbose_name='номер версии')
    title = models.CharField(max_length=150, verbose_name='название')
    is_active = models.BooleanField(choices=[(True, 'active'), (False, 'not active')], verbose_name='признак активности')

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Version_detail", kwargs={"pk": self.pk})

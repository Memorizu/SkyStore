from django.db import models
from catalog.models import Category
from users.models import User


NULLABLE = {'blank': True, 'null': True}

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена за покупку')
    create_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    last_change_date = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name='пользователь')
    
    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

from django.db import models
from catalog.models import NULLABLE


NULLABLE = {'blank': True, 'null': True}


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    phone = models.CharField(max_length=100, verbose_name='телефон')
    message = models.TextField(**NULLABLE, verbose_name='Адрес')

    def __str__(self):
        return f'{self.name} - {self.phone}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
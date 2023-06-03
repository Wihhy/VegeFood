from django.db import models
from uuid import uuid4


class Product(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=50, verbose_name='Назва')
    description = models.TextField(verbose_name='Опис')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Ціна')
    is_available = models.BooleanField(default=True, verbose_name='Доступність')
    image = models.ImageField(upload_to='product_image', null=False, verbose_name='Фото')
    category = models.CharField(max_length=50, verbose_name='Категорія')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

# class Order(models.Model):








from django.db import models
from uuid import uuid4
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name='Категорія')
    image = models.ImageField(upload_to='category_image', null=False, verbose_name='Фото')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категорії'
        ordering = ('name',)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=50, verbose_name='Назва')
    description = models.TextField(verbose_name='Опис')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Ціна')
    in_stock = models.IntegerField(default=0, verbose_name='На складі')
    image = models.ImageField(upload_to='product_image', null=False, verbose_name='Фото')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=False,
                                 verbose_name='Категорія')
    discount = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=True, verbose_name='Ціна зі знижкою')
    slug = models.SlugField(unique=True, allow_unicode=True)  # TODO не створюється автоматично

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
        ordering = ('category', 'name')









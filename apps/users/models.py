from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    country = models.CharField(max_length=20, null=True, blank=True, verbose_name='Країна')
    city = models.CharField(max_length=20, null=True, blank=True, verbose_name='Місто')
    street_address = models.CharField(max_length=50, null=True, blank=True, verbose_name='Вулиця та номер дому')
    postcode = models.CharField(max_length=20, null=True, blank=True, verbose_name='Поштовий індекс')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефону',
                                    help_text='Формат телефону: (xxx) xxx-xxxx', null=True, blank=True)

    def __str__(self):
        return str(f'{self.last_name} {self.first_name}')

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Профіль'
        verbose_name_plural = 'Профілі'



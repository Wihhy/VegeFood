# Generated by Django 4.2.1 on 2023-06-08 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True),
        ),
    ]
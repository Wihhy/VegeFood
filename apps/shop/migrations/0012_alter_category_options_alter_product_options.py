# Generated by Django 4.2.1 on 2023-06-07 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_product_options_product_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('category', 'name'), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товари'},
        ),
    ]

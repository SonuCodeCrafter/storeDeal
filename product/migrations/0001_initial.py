# Generated by Django 5.1.4 on 2024-12-27 12:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the unique the name of the category', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the product such that(iphone 12, lenovo charger)', max_length=255)),
                ('price', models.DecimalField(decimal_places=3, help_text='Enter the price of the product', max_digits=10)),
                ('stock_quantity', models.PositiveIntegerField(help_text='Enter the Quantity of the product')),
                ('category', models.ForeignKey(help_text='Select the Category of the particular product', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.category')),
            ],
        ),
    ]

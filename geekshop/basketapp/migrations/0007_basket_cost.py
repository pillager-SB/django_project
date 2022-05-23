# Generated by Django 3.2.13 on 2022-05-08 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0006_remove_basket_products_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='цена продукта'),
        ),
    ]
# Generated by Django 3.2.13 on 2022-04-25 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.category', verbose_name='категория продукт'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=140, verbose_name='описание продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product_images', verbose_name='изображение продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=25, unique=True, verbose_name='имя продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='цена продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='количество на складе'),
        ),
    ]

from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='имя категории', max_length=25, unique=True)
    description = models.TextField(verbose_name='описание категории', max_length=140, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}: {self.name}"


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='категория продукт', on_delete=models.DO_NOTHING)
    name = models.CharField(verbose_name='имя продукта', max_length=25, unique=False)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    image = models.ImageField(verbose_name='изображение продукта', upload_to='product_images')
    price = models.DecimalField(verbose_name='цена продукта', max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    def can_add_to_basket(self, user):
        pass
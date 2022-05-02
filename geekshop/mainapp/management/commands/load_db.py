import json
from django.core.management.base import BaseCommand
from django.conf import settings
from mainapp.models import Category, Product
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model


def load_from_json(file_name):
    with open(settings.DATA_ROOT / file_name, 'r', encoding='utf-8') as f:
        return json.load(f)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories.json')
        for category_data in categories:
            try:
                category = Category(**category_data)
                category.save()
            except IntegrityError:
                pass

        products = load_from_json('products.json')
        for product_data in products:
            product_data['category'] = Category.objects.get(name=product_data['category'])
            product = Product(**product_data)
            product.save()

        User = get_user_model()
        if not User.objects.filter(username='nadmin'):
            User.objects.create_superuser(username='nadmin', password='admin')

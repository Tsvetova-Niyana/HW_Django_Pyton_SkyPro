import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def delete_everything(self):
        Product.objects.all().delete()
        Category.objects.all().delete()

    def handle(self, *args, **options):
        self.delete_everything()

        with open('new_category.json', encoding='utf-8') as f:
            category_list = json.load(f)

            category = []

            count_cat = 0
            for cat in category_list:
                category.append(Category(
                    id=count_cat + 1,
                    category_name=cat["category_name"],
                    description=cat["description"]
                ))
                count_cat += 1

            Category.objects.bulk_create(category)

        with open('new_product.json', encoding='utf-8') as f:
            product_list = json.load(f)

            product = []

            count_prod = 0
            for prod in product_list:
                product.append(Product(
                    id=count_prod + 1,
                    name_product=prod["name_product"],
                    description=prod["description"],
                    category_id=prod["category"],
                    amount=prod["amount"]
                ))
                count_prod += 1

            Product.objects.bulk_create(product)

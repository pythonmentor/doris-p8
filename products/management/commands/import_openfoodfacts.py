""" Import data from openfoodfacts API to the app database"""

import requests
import json
from django.core.management.base import BaseCommand, CommandError
from products.models import Category, Product

help = 'Import data from openfoodfacts API to the app database'


cats_to_add = [
"biscuits et gâteaux", "pizzas", "pâtes à tartiner aux noisettes", "glaces",
"chocolats", "sodas", "bonbons", "chips", "céréales", "fromages", "confitures",
"jus de fruits", "desserts lactés", "soupes", "lasagnes", "miels",
"galettes de céréales", "rillettes", "bières", "hummus", "brioches", "sandwichs"
]

grades = [
"a", "b", "d", "e"
]

criteria = {
    "action": "process",
    "tagtype_0": "categories",
    "tag_contains_0": "contains",
    "tagtype_1": "nutrition_grades",
    "tag_contains_1": "contains",
    "page_size": "1",
    "json": "1",
}

url = "https://fr.openfoodfacts.org/cgi/search.pl"

class Command(BaseCommand):
    """ Import openfoodfacts datas """

    def import_category(self, category):
        """ Get the categories from my predefined list """
        cat,created = Category.objects.get_or_create(
        name_cat=category
        )
        cat.save()

    def import_product(self, data, category):
        """ Collect OFF products according to the predefined categories """

        for data_product in data['products']:
            name_prod = data_product.get('product_name', None)
            nutrition_grade = data_product.get('nutrition_grades', None)
            rep_nutritionnel = data_product.get('image_nutrition_url', None)
            image = data_product.get('image_url', None)
            url = data_product.get('url', None)
            category = Category.objects.get(name_cat=category)
            if name_prod == None or nutrition_grade == None or rep_nutritionnel == None or image == None or url == None or category == None:
                continue
            else:
                try:
                    prod,created = Product.objects.get_or_create(
                    name_prod = name_prod,
                    nutrition_grade = nutrition_grade,
                    rep_nutritionnel = rep_nutritionnel,
                    image = image,
                    url = url,
                    category = category
                    )
                    if created:
                        prod.save()
                        print('bien joué !')
                        display_format_prod = "Product, {} , a bien été enregistré"
                        print(display_format_prod.format(name_prod))

                except Product.DoesNotExist:
                    raise CommandError("Product %s n'a pas été trouvé" % name_prod)

    def handle(self, *args, **options):
        """ GET request to the  API """

        for cat in cats_to_add:
            self.import_category(cat)
            criteria['tag_0'] = cat
            for tag in grades:
                criteria['tag_1'] = tag
                response = requests.get(url, params=criteria)

                products = response.json()

                self.import_product(products, cat) 

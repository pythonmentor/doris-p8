from django.test import TestCase
from .models import Product, Category

class ProductModelTest(TestCase):
    """ Test for import in database and Product & Category """
    def setUp(self):
        cat = Category.objects.create(
            name_cat = 'yaourt',
        )

        Product.objects.create(
                name_prod='test product',
                nutrition_grade='b',
                rep_nutritionnel='https://static.openfoodfacts.org/images/products/376/020/616/0102/ingredients_fr.12.full.jpg',
                image = 'https://static.openfoodfacts.org/images/products/376/020/616/0102/front_fr.11.full.jpg',
                url = 'https://fr.openfoodfacts.org/produit/3760206160102/yaourt-artisanal-noix-de-coco-ibaski',
                category = Category.objects.get(name_cat=cat))

    def test_add_product(self):
        product = Product.objects.get(id=1)
        expected_product_name = f'{product.name_prod}'

        self.assertEqual(expected_product_name, 'test product')

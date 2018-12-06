from django.test import TestCase
from django.contrib.auth import get_user_model
from products.models import Product, Category, Favorite
from django.test import Client
from django.contrib.auth.models import User
from django.urls import reverse

class TestSearchView(TestCase):
    """ All the tests for Search view """
 #test search unhealthy product to send to jquery
    def setUp(self):
        cat = Category.objects.create(
             name_cat = 'yaourt',
         )

        e_product = Product.objects.create(
                 name_prod='test product',
                 nutrition_grade='e',
                 rep_nutritionnel='https://static.openfoodfacts.org/images/products/376/020/616/0102/ingredients_fr.12.full.jpg',
                 image = 'https://static.openfoodfacts.org/images/products/376/020/616/0102/front_fr.11.full.jpg',
                 url = 'https://fr.openfoodfacts.org/produit/3760206160102/yaourt-artisanal-noix-de-coco-ibaski',
                 category = Category.objects.get(name_cat=cat)
        )

        a_product = Product.objects.create(
                 name_prod='test product 2',
                 nutrition_grade='a',
                 rep_nutritionnel='https://static.openfoodfacts.org/images/products/345/020/616/0102/ingredients_fr.12.full.jpg',
                 image = 'https://static.openfoodfacts.org/images/products/345/020/616/0102/front_fr.11.full.jpg',
                 url = 'https://fr.openfoodfacts.org/produit/3760206160103/yaourt-artisanal-noix-de-coco-ibaski',
                 category = Category.objects.get(name_cat=cat)
        )

        e_product_2 = Product.objects.create(
                 name_prod='test 3',
                 nutrition_grade='e',
                 rep_nutritionnel='https://static.openfoodfacts.org/images/products/376/020/616/0103/ingredients_fr.12.full.jpg',
                 image = 'https://static.openfoodfacts.org/images/products/376/020/616/0103/front_fr.11.full.jpg',
                 url = 'https://fr.openfoodfacts.org/produit/3760206160103/yaourt-artisanal-noix-de-coco-ibaski',
                 category = Category.objects.get(name_cat=cat)
        )

        User.objects.create(
        first_name='user_test',
        username='utilisateur@gmail.com',
        password='mot_de_passe'
        )
        self.users = User.objects.get(first_name="user_test")

        Favorite.objects.create(
        product=e_product,
        substitute=a_product,
        user=self.users
        )
        self.subs = Favorite.objects.get(substitute=a_product)


    def test_search_unhealthy(self):
        get_product = Product.objects.filter(
            nutrition_grade__range = ('d','e'), name_prod__icontains = 'test product')
        for item in get_product:
            my_product = f'{item.name_prod}'

        self.assertEqual(my_product, 'test product')

 #test query js avec selenium


 #test search healthy product
    def test_search_healthy(self):
        get_product = Product.objects.filter(
            nutrition_grade__range = ('a','b'), name_prod__icontains = 'test product 2')
        for item in get_product:
            my_product = f'{item.name_prod}'

        self.assertEqual(my_product, 'test product 2')

 #test search page is called
    def test_uses_search_template(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)

#test detail page - product exists
    def test_product_detail_view_exist(self):
        id_exist = Product.objects.get(name_prod='test product').id
        response = self.client.get(reverse('search:details', args=(id_exist,)))
        self.assertEqual(response.status_code, 200)

#test detail page - product doesn't exist
    # def test_product_detail_view_doesnt_exist(self):
    #     id_doesnt_exist = Product.objects.last().id + 1
    #     response = self.client.get(reverse('search:details', args=(id_doesnt_exist,)))
    #     self.assertEqual(response.status_code, 404)


#test favorite page - get favorite for a specific user
    def test_get_favorite(self):
        subs_id = self.subs.id
        response = self.client.get('favorite', args=(subs_id,))
        fav = Favorite.objects.first()
        self.assertEqual(self.users, fav.user)

from django.test import TestCase
from django.contrib.auth import get_user_model
from products.models import Product, Category, Favorite
from django.test import Client

class TestSearchView(TestCase):
    """ All the tests for Search view """
 #test recherche unhealthy
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

    def test_search_unhealthy(self):
        get_product = Product.objects.filter(
            nutrition_grade__range = ('d','e'), name_prod__icontains = 'test product')
        for item in get_product:
            my_product = f'{item.name_prod}'

        self.assertEqual(my_product, 'test product')

 #test query js avec selenium


 #test recherche healthy
    def test_search_healthy(self):
        get_product = Product.objects.filter(
            nutrition_grade__range = ('a','b'), name_prod__icontains = 'test product 2')
        for item in get_product:
            my_product = f'{item.name_prod}'

        self.assertEqual(my_product, 'test product 2')

 #test page search est appelée
    def test_uses_search_template(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)

#test page detail product inexistant
    # def test_product_detail_view(self):
    #     id = 17
    #     id_2 = 10000
    #     response = self.client.get('/search/details/<int:id>/')
    #     no_response = self.client.get('/search/details/<int:id_2>/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(no_response.status_code, 404)


 #test pour vrifier que login necessaire pour accéder à la vue favorite
    # def test_access_favorite(self):
    #     self.user = get_user_model().objects.create_user(
    #         first_name = 'didi',
    #         username = 'dodo@hotmail.fr',
    #         password = 'secret'
    #     )
    #     u = Client()
    #     u.login(username = 'dodo@hotmail.fr', password = 'secret')
    #     response = u.get('/search/favorite/')
    #     self.assertEqual(response.status_code, 200)

 #test pour recherche dans favorite

    def test_get_favorite(self):
        cat = Category.objects.create(
             name_cat = 'pomme',
         )

        e_product = Product.objects.create(
                 name_prod='test product',
                 nutrition_grade='e',
                 rep_nutritionnel='https://static.openfoodfacts.org/images/products/376/020/616/0102/ingredients_fr.12.full.jpg',
                 image = 'https://static.openfoodfacts.org/images/products/376/020/616/0102/front_fr.11.full.jpg',
                 url = 'https://fr.openfoodfacts.org/produit/3760206160102/yaourt-artisanal-noix-de-coco-ibaski',
                 category = Category.objects.get(name_cat=cat)
        )
        u = Client()

        test_fav = Favorite.objects.filter(id = 1)
        for item in test_fav:
            get_fav_page = f'{item.name_prod}'

            self.assertEqual(get_fav_page, 'test product')


 #test pour enregistrer dans favorite
    # def test_save_product(self):
    #     cat = Category.objects.create(
    #          name_cat = 'thing',
    #      )
    #     user = Client()
    #     user_test = user.login(username='utilisateur', password='mot_de_passe')
    #
    #
    #     product_exists = Product.objects.create(
    #              name_prod='test product exist',
    #              nutrition_grade='a',
    #              rep_nutritionnel='https://static.openfoodfacts.org/images/products/372/020/616/0102/ingredients_fr.12.full.jpg',
    #              image = 'https://static.openfoodfacts.org/images/products/372/022/616/0102/front_fr.11.full.jpg',
    #              url = 'https://fr.openfoodfacts.org/produit/376020616/ytest-product-exist',
    #              category = Category.objects.get(name_cat=cat),
    #              users = user_test.set()
    #     )
    #     favorite = Favorite(
    #         product_id = 1,
    #         substitute_id = product_exists.id,
    #         users = 1)
    #     favorite.save()
    #     self.assertEqual(product_exists, 'test product exist')



  #test pour supprimer dans favorite

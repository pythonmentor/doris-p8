from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from products.models import Category, Product, Favorite
from django.contrib.auth.models import User
import random
import json
from django.contrib.auth.decorators import login_required



def search_function(request):
    """ Get the user input of products and search unhealthy propositions in
     the database """
    #show unhealthy product and return a json for autocomplete with jquery UI
    if request.method == 'GET':
        query = request.GET.get('term', '')
        unhealthy_prod = Product.objects.filter(
            nutrition_grade__range = ('d','e'), name_prod__icontains = query)
        results = []

        for prod in unhealthy_prod:
            results.append(prod.name_prod)
        data = json.dumps(results)
        mimetype = 'application/json'

        return HttpResponse(data, mimetype)

    #get healthy products from the same category than the unhealthy product selected
    if request.method == 'POST':
        choice = request.POST.get('txtSearch')
        for item in Product.objects.filter(name_prod=choice):
            cat = item.category

        healthy_prod = Product.objects.filter(
            category = cat, nutrition_grade__in = ('a','b','c')).order_by(
            'nutrition_grade'
            )[:6]

        #create variable with unhealthy products info to render in the template
        title = "[ Résultats pour la recherche: %s ]"%choice
        choice_image = item.image
        choice_name = item.name_prod
        choice_id = item.id
        products = []

        #create variable with healthy products info to render in the template
        for item in healthy_prod:
            product = {
                'name': item.name_prod,
                'grade': item.nutrition_grade,
                'image': item.image,
                'id': item.id
            }
            products.append(product)

        #render all the information in the template
        results = {
            'title': title,
            'choice_id': choice_id,
            'choice_name': choice_name,
            'choice_image': choice_image,
            'products': products
        }

        return render(request, 'search/search.html', results)


def display_details(request, id_healthy):
    """ Display the details about a product on a dedicated page """
    if request.method == 'GET':

        details = []
        for item in Product.objects.filter(id=id_healthy):
            details_list = {
                'name' : item.name_prod,
                'image': item.image,
                'grade': item.nutrition_grade,
                'rep': item.rep_nutritionnel,
                'url': item.url
            }
            details.append(details_list)

            results = {
                'details' : details
            }

        return render(request, 'search/details.html', results)


@login_required
def save_product(request):
    """ Save favorite products and their substitutes through Search page"""
    #get the id of the healthy product chosen by the user and the unhealthy product and save it in Favorite table
    if request.method == 'POST':
        id_favorite = request.POST.get('id_healthy')
        unhealthy_choice = request.POST.get('id_unhealthy')

        favorite = Favorite.objects.filter(
            product_id = unhealthy_choice,
            substitute_id = id_favorite,
            user = request.user).exists()

        if favorite == True:
            save_event = {
                "validation" : "exists",
            }

        elif favorite == False:
            favorite = Favorite(
                product_id = unhealthy_choice,
                substitute_id = id_favorite,
                user = request.user)
            favorite.save()
            #render the information to jQuery for the button event
            save_event = {
                "validation" : "save",
            }

        return HttpResponse(json.dumps(save_event), content_type="application/json")


@login_required
def remove_product(request):
    """ Delete favorite products from database through Favorite page """
    #get the id of the healthy product chosen by the user and remoce it from database
    #créer la vue Remove en mettant en gabarit les id des produits healthy et unhealthy
    if request.method == 'POST':
        delete_id_favorite = request.POST.get('delete_favorite')
        delete_id_unhealthy = request.POST.get('delete_unhealthy')

        # for item in Favorite.objects.filter(substitute_id=delete_id_favorite):
        #     test = item.substitute
        #     print('test', test)

        delete_fav = Favorite.objects.get(
            substitute_id = delete_id_favorite,
            product_id = delete_id_unhealthy,
            user = request.user).delete()

        #render the information to jQuery for the button event
        remove_event = {
            "validation" : "delete",
        }

        return HttpResponse(json.dumps(remove_event), content_type="application/json")
        #renvoyer la vue en guise de réponse


def favorite_display(request):
    """ Display the favorite products for each user through Favorite page """
    if request.method == 'GET':
        #get the information to display from Product table filtered by user
        user = request.user
        get_favorite = Product.objects.filter(
            users = user).order_by(
            'nutrition_grade'
            )
        favorites = []
        #get unhealthy product id from Favorite table, filtered with the substitute id
        for fav in get_favorite:
            get_id_unhealthy = Favorite.objects.filter(
                user = user, substitute_id = fav.id).order_by(
                'product__nutrition_grade')
            for fav_unhealthy in get_id_unhealthy:
                id_fav_unhealthy = fav_unhealthy.product_id

            favorite = {
                'id_substitute': fav.id,
                'id_product': id_fav_unhealthy,
                'fav_user': fav.users,
                'fav_product': fav.name_prod,
                'fav_image': fav.image,
                'fav_grade': fav.nutrition_grade
            }
            favorites.append(favorite)

        results = {
            'favorites': favorites
        }

        return render(request, 'search/favorite.html', results)

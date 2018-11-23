from django.shortcuts import render
from django.http import HttpResponse
from products.models import Category, Product, Favorite
from django.contrib.auth.models import User
import random
import json
from django.contrib.auth.decorators import login_required



def search_function(request):
    """ Get the user input of products and search unhealthy propositions in
     the database """
    #show unhealthy product
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
            category = cat, nutrition_grade__in = ('a','b','c'))

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


# @login_required
def save_product(request):
    """ Save favorite products and their substitutes """
    #get the id of the healthy product chosen by the user and the unhealthy product and save it in Favorite table
    if request.method == 'POST':
        id_favorite = request.POST.get('id_healthy')
        unhealthy_choice = request.POST.get('id_unhealthy')
        favorite = Favorite(
            product_id = unhealthy_choice,
            substitute_id = id_favorite,
            user = request.user)
        favorite.save()

        #render the information to jQuery fo the button event
        save_event = {
            "validation" : "pass",
        }
        test = print('goooood !!')
        #if id_favorite == favorite.substitute_id:
            #favorite.delete()

        #save_event = {
            #"validation": "fail",
        #}

        return HttpResponse(json.dumps(save_event), content_type="application/json")

# @login_required
# def remove_product(request):
#     """ Delete favorite products from database """
#     if request.method == 'POST':
#         pass

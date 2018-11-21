from django.shortcuts import render
from django.http import HttpResponse
from products.models import Category, Product
import random
import json


#@login_required(login_url='/connection/')
def search_function(request):
    """ Get the user input of products and search unhealthy propositions in
     the database """
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

    if request.method == 'POST':
        choice = request.POST.get('txtSearch')
        for item in Product.objects.filter(name_prod=choice):
            cat = item.category

        healthy_prod = Product.objects.filter(
            category = cat, nutrition_grade__in = ('a','b','c'))

        title = "[ Résultats pour la recherche: %s ]"%choice
        choice_image = item.image
        products = []

        for item in healthy_prod:
            product = {
                'name': item.name_prod,
                'grade': item.nutrition_grade,
                'image': item.image
            }
            products.append(product)

        results = {
            'title': title,
            'choice_image': choice_image,
            'products': products
        }

        return render(request, 'search/search.html', results)

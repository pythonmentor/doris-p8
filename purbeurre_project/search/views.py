from django.shortcuts import render
from django.http import HttpResponse
from products.models import Category, Product
import random
import json
from search.forms import SearchForm




#@login_required(login_url='/connection/')
def search_function(request):
    """ Get the user input of products and search unhealthy propositions in
     the database """
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['product'] #field from my form

            id_cat = Product.objects.filter(
                nutrition_grade__range = ('d','e'), name_prod__icontains = query).values(
                'category')
            get_cat = {
                'category': id_cat
            }

            #transform the request into list to extract category number
            get_cat_list = list(get_cat['category'])
            selection = random.choice(get_cat_list)
            cat = selection.get('category')
            print('category', cat)

            #request to get healthy products from the foreign key
            healthy_request = Product.objects.filter(
                nutrition_grade__range = ('a','b')). filter(
                category = cat).values(
                'name_prod', 'image'
                )
            print('requete', healthy_request)
            title = "Résultats pour la requête %s"%query
            #turn the results into a list to display in frontend
            context = {
                'name_prod': 'name_prod',
                'image': 'image'
            }

            if not id_cat.exists():
                title = 'Désolé, pas de résultats pour cette recherche'

            return render(request, 'search/search.html', context)

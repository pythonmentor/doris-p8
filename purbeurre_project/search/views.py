from django.shortcuts import render
from django.http import HttpResponse
from products.models import Category, Product
import random
import json


#@login_required(login_url='/connection/')
def search_function(request):
    """ Get the user input of products and search unhealthy propositions in
     the database """
    if request.method == 'POST':
        query = request.GET.get('term', '')
        print(query)
        unhealthy_prod = Product.objects.filter(name_prod__icontains = query)
        results = []

        for prod in unhealthy_prod:
            results.append(prod.name_prod)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'

    return HttpResponse(data, mimetype)

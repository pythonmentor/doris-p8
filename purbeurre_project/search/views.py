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

# def get_results(request):
#     """ Get and display healthy results """
#     if request.method == 'GET':
#         # choices = request.GET.get('search','None')
#         print('ok')
#         # unhealthy = search_function()
#         # print('hello')
#         # test = unhealthy.Category.all()
#         #
#         # cat = print(test)
#
#         return render(request, 'search/search.html')

from django.shortcuts import render
from products.models import Category, Product



#@login_required(login_url='/connection/')
class QueryAutocomplete():
    def search_function(request):
        """ Get the user input of products and search unhealthy propositions in
         the database """
        query = request.GET.get('query')
        product_name = Product.objects.filter(
            nutrition_grade__range = ('d','e')).filter(
            name_prod__icontains = query).values_list(
            'name_prod', 'image', named=True)

    # def results_function(request):
    #     """ Return healthy propositions to the user input """

        title = "Résultats pour la requête %s"%query
        context = {
            'product_name': product_name,
        }
        print(context)
        if not product_name.exists():
            title = 'Désolé, pas de résultats pour cette recherche'


        return render(request, 'search/search.html', context)

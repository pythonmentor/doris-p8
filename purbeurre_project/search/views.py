from dal import autocomplete
from django.shortcuts import render
from users.models import Category, Product



#@login_required(login_url='/connection/')
class QueryAutocomplete(autocomplete.Select2QuerySetView):
    def search_function(request):
        """ Get the user input of products and return search results """
        query = request.GET.get('query')
        grade = Product.objects.filter(nutrition_grade = 'e').filter(name_prod__icontains=query)
        return HttpResponse(template.render(request=grade))

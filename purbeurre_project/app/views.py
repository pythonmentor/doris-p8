from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def home(request):
    """ Get the homepage """
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(request=request))

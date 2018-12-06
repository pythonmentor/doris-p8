from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def home(request):
    """ Get the homepage """
    template = loader.get_template('app/index.html')

    return HttpResponse(template.render(request=request))

def mentions(request):
    """ Display the legal mentions """
    if request.method == 'GET':
        template = loader.get_template('app/mentions-legales.html')

        return HttpResponse(template.render(request=request))

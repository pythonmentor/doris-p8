from django.urls import path, include
from search import views
from . import views

app_name = 'search'

urlpatterns = [
    path('search/', views.search_function, name='search'),
    path('search/', views.get_results, name='results'),
]

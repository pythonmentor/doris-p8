from django.urls import path, include
from search import views

app_name = 'search'

urlpatterns = [
    path('search/', views.search_function, name='search'),
    path('ajax_calls/search/', autocompleteModel),
]

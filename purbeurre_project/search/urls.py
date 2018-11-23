from django.urls import path, include
from search import views
from . import views

app_name = 'search'

urlpatterns = [
    path('', views.search_function, name='search'),
    path('record_favorite', views.save_product, name='save'),
    path('remove_favorite', views.remove_product, name='remove')
]

from django.urls import path, include
from search import views
from . import views

app_name = 'search'

urlpatterns = [
    path('', views.search_function, name='search'),
    path('no_product', views.no_product, name='no-product'),
    path('record_favorite', views.save_product, name='save'),
    path('remove_favorite', views.remove_product, name='remove'),
    path('favorite', views.favorite_display, name='favorite'),
    path('details/<int:id_healthy>/', views.display_details, name='details')
]

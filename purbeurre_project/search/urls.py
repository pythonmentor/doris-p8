from django.urls import path, include
from search import views

app_name = 'search'

urlpatterns = [
    path('search/', views.QueryAutocomplete.search_function, name='search'),
    path('select2/', include('django_select2.urls')),
]

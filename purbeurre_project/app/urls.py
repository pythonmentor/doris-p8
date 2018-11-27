from django.urls import path
from app import views


app_name = 'app'

urlpatterns = [
    path('accueil/', views.home, name='index'),
    path('mentions-legales/', views.mentions, name='mentions')
]

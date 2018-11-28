from django.urls import path
from users import views
from . import views
from django.conf import settings

app_name = 'users'

urlpatterns = [
    path('account/', views.myaccount, name='account'),
    path('connection/', views.connection, name='connection'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.create_user, name='registration')
]

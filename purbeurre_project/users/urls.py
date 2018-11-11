from django.urls import path
from users import views
from . import views

app_name = 'users'

urlpatterns = [
    path('my-account/', views.myaccount, name='myaccount'),
    path('connection/', views.connection, name='connection'),
    path('deconnection/', views.deconnection, name='deconnection'),
    path('register/', views.create_user, name='registration')
]

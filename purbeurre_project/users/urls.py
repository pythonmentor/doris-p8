from django.urls import path
from users import views
from . import views

app_name = 'users'

urlpatterns = [
    path('account/', views.myaccount, name='account'),
    path('connection/', views.connection, name='connection'),
    # path('logout/', views.logout_view, name='logout'),
    path('register/', views.create_user, name='registration')
]

from django.contrib import admin
from .models import Category, Product, Favorite

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Favorite)

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name_cat = models.CharField(max_length=250)
    def __str__(self):
        return str(self.name_cat)

class Product(models.Model):
    name_prod = models.CharField(max_length=250)
    nutrition_grade = models.CharField(max_length=1)
    rep_nutritionnel = models.URLField()
    image = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="related category", related_name='products')
    users = models.ManyToManyField(User, verbose_name="related favorites", related_name='favorite_products', through='Favorite', through_fields=('substitute','user')) #through to link to intermediary table
    def __str__(self):
        return str(self.name_prod)

class Favorite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="related product details", related_name='favorite_products')
    substitute = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="related substitute", related_name='favorite_substitute',)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="related user")
    def __str__(self):
        return f"{self.substitute} - {self.user}" #used en admin

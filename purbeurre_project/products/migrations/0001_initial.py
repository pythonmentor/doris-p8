# Generated by Django 2.1.3 on 2018-11-11 07:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cat', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_prod', models.CharField(max_length=250)),
                ('nutrition_grade', models.CharField(max_length=1)),
                ('rep_nutritionnel', models.URLField()),
                ('image', models.URLField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category', verbose_name='related category')),
                ('users', models.ManyToManyField(related_name='favorite_products', through='products.Favorite', to=settings.AUTH_USER_MODEL, verbose_name='related favorites')),
            ],
        ),
        migrations.AddField(
            model_name='favorite',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_products', to='products.Product', verbose_name='related product details'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='substitute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_substitute', to='products.Product', verbose_name='related substitute'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='related user'),
        ),
    ]

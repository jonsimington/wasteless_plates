from django.db import models


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=250)
    serving_size = models.IntegerField(default=0)
    nutrition = models.OneToOneField('Nutrition')


class Ingredients(models.Model):
    recipe = models.ForeignKey('Recipe')
    name = models.CharField(max_length=75)
    unit = models.CharField(max_length=25)
    amount = models.IntegerField(default=0)


class Nutrition(models.Model):
    calories = models.IntegerField(default=0)
    total_fat = models.IntegerField(default=0)
    sodium = models.IntegerField(default=0)
    sugar = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)

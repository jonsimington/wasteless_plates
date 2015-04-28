from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=250)
    serving_size = models.IntegerField(default=0)
    bigoven_id = models.IntegerField(unique=True)
    nutrition_info = models.OneToOneField('Nutrition', null=True)

    def __str__(self):
        return self.recipe_name


@python_2_unicode_compatible
class Ingredient(models.Model):
    recipe = models.ForeignKey('Recipe')
    item = models.ForeignKey('Item')
    unit = models.CharField(max_length=10, null=True)
    amount = models.FloatField(default=0)

    def __str__(self):
        return self.item.name



@python_2_unicode_compatible
class Nutrition(models.Model):
    calories = models.IntegerField(default=0)
    total_fat = models.IntegerField(default=0)
    sodium = models.IntegerField(default=0)
    sugar = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)

    def __str__(self):
        return self.id



@python_2_unicode_compatible
class Item(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name



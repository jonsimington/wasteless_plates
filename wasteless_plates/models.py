from django.db import models


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=250)
    serving_size = models.IntegerField(default=0)


class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient_name = models.CharField(max_length=75)
    ingredient_unit = models.CharField(max_length=25)
    ingredient_amount = models.IntegerField(default=0)

class Nutrition(models.Model):
    recipe = models.ForeignKey(Recipe)
    nutrition_calories = models.IntegerField(default=0)
    nutrition_totalFat = models.IntegerField(default=0)
    nutrition_satFat = models.IntegerField(default=0)
    nutrition_transFat = models.IntegerField(default=0)
    nutrition_cholesterol = models.IntegerField(default=0)
    nutrition_sodium = models.IntegerField(default=0)
    nutrition_dietaryFiber = models.IntegerField(default=0)
    nutrition_sugars = models.IntegerField(default=0)
    nutrition_protein = models.IntegerField(default=0)
    nutrition_vitaminA = models.IntegerField(default=0)
    nutrition_vitaminC = models.IntegerField(default=0)
    nutrition_calcium = models.IntegerField(default=0)
    nutrition_iron = models.IntegerField(default=0)

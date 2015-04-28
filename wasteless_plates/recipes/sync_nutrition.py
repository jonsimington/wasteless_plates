from models import Recipe

import requests, json

api_key = 'KWnEYhUmW8lSBur289GCHCCZaE4t7bCAkD31bPrE'

# all recipes that don't currently have nutrition info
# used to minimize USDA API calls
recipes = Recipe.objects.filter(nutrition_info=None)

for recipe in recipes:
    # macronutrient values
    sugar = 0    # grams     id=205
    fat = 0      # grams     id=204
    calories = 0 # kcal      id=208
    sodium = 0   # miligrams id=307
    protein = 0  # g         id=203

    # get approximate macros for each ingredient
    for ingredient in recipe.ingredient_set.all():
        # USDA food search API call
        url="http://api.nal.usda.gov/usda/ndb/search/?format=json&q=" + ingredient.item.name + "&api_key=" + api_key + "&max=1"
        r = requests.get(url)
        ingredient_json = json.loads(r.text)
        
        # id of ingredient in USDA db
        ndbno = ingredient_json['list']['item'][0]['ndbno']
        
        # USDA nutrient API call
        ingredient_url = "http://api.nal.usda.gov/usda/ndb/nutrients/?format=json&api_key=" + api_key + "&nutrients=205&nutrients=204&nutrients=208&nutrients=307&nutrients=203&ndbno=" + ndbno
        
        r = requests.get(ingredient_url)
        nutrient_json = json.loads(r.text)
        
        # add ingredient's macro values to the total for the recipe
        sugar += (float(nutrient_json['report']['foods'][0]['nutrients'][3]['value']) * ingredient.amount)
        fat += (float(nutrient_json['report']['foods'][0]['nutrients'][1]['value']) * ingredient.amount)
        calories += (float(nutrient_json['report']['foods'][0]['nutrients'][4]['value']) * ingredient.amount)
        sodium += (float(nutrient_json['report']['foods'][0]['nutrients'][2]['value']) * ingredient.amount)
        protein += (float(nutrient_json['report']['foods'][0]['nutrients'][0]['value']) * ingredient.amount)
        

    # set macronutrient amounts for the recipe
    recipe.nutrition_info.sugar = sugar
    recipe.nutrition_info.total_fat = fat
    recipe.nutrition_info.sodium = sodium
    recipe.nutrition_info.calories = calories
    recipe.nutrition_info.protein = protein

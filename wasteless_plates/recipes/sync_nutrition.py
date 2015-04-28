#from models import Recipe

import requests

api_key = 'v49BzRIFAfUpB7vFZzNWzgpS1RWANOcmsRLAap44'

# all recipes that don't currently have nutrition info
# used to minimize wolframalpha API calls
#recipes = Recipe.objects.filter(nutrition_info=None)

url="http://api.nal.usda.gov/usda/ndb/search/?format=json&q=" + 'carrot' + "&api_key=" + api_key + "?max=1"

r = requests.get(url)

print(r)

"""
for recipe in recipes:
    # macronutrient values
    calories = 0
    fat = 0
    sodium = 0
    sugar = 0
    protein = 0

    # get macros for each ingredient
    for ingredient in recipe.ingredient_set.all():
        res = client.query('temperature in Washington, DC on October 3, 2012')
"""

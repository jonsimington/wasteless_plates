# Another hack
import django
django.setup()

from wasteless_plates.recipes.models import Recipe, Nutrition

import requests, json, time

api_key = 'M3P1ZmPNwITFFonnYnKBcVEoYMLEaodhDiOjb0xQ'

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
        print (ingredient)
        url="http://api.nal.usda.gov/usda/ndb/search/?format=json&q=" + ingredient.item.name + "&api_key=" + api_key + "&max=1"
        r = requests.get(url)
        
        # make sure we aren't over api limit
        remaining = r.headers['X-RateLimit-Remaining']
        print("API CALLS REMAINING:", int(remaining))
        
        if "OVER" in r.text:
            print("too fast, waiting 15 seconds")
            time.sleep(15)
        if int(remaining) < 20:
            print("too many api accesses, waiting 1 hour 10 mins")
            # wait 1 hr 10 mins
            time.sleep(4200)
            
        ingredient_json = json.loads(r.text)
        print(ingredient_json)
        
        # id of ingredient in USDA db
        try:
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
            
            # create nutrition object with the values determined from food search
            recipe.nutrition_info = Nutrition.objects.create(calories=calories, total_fat=fat, sodium=sodium, sugar=sugar, protein=protein)
            recipe.save()
        
        except:
            continue
            

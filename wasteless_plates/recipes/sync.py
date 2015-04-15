__author__ = 'connor'

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wasteless_plates.settings")

# Python imports
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

# Local imports
from wasteless_plates.recipes.models import Ingredient, Recipe

# BigOven API Key
API_KEY = 'dvxU8G36Kk30y4nP340XnQ0VL8RdJQpF'

# Base URL
BASE_SEARCH_URL = 'http://api.bigoven.com/recipes?'
BASE_GET_URL = 'http://api.bigoven.com/recipe/'

## URL Parameters
# Searching for a bulk number of recipes
SEARCH_URL_PARAMS = { # All parameters available http://api.bigoven.com/documentation/recipe-search-results
    'api_key': API_KEY,
    'pg': '',
    'rpp': '',
    'sort': 'quality'
}
# Retrieving specific recipe
GET_URL_PARAMS = {
    'api_key': API_KEY,
}


# One run command for syncing recipes to the database
def sync_all(page, results_per_page):
    # Build our search parameters
    SEARCH_URL_PARAMS['pg'] = page
    SEARCH_URL_PARAMS['rpp'] = results_per_page

    # Build url and query
    params = urllib.parse.urlencode(SEARCH_URL_PARAMS)
    page = urllib.request.urlopen((BASE_SEARCH_URL + '%s') % params)

    # Parse from xml into etree
    data = ET.fromstring(page.read().decode())

    # For each recipe in search results
    for recipe in data.iter('RecipeInfo'):
        # Print recipe number and sync
        print(recipe.find('RecipeID').text)
        sync_recipe(recipe)


# Sync individual recipe
def sync_recipe(r):
    # Build our search parameters and modify url
    params = urllib.parse.urlencode(GET_URL_PARAMS)
    NEW_GET_URL = BASE_GET_URL + r.find('RecipeID').text + '?'

    # Build url and query
    page = urllib.request.urlopen((NEW_GET_URL + '%s') % params)

    # Parse from xml into etree
    data = ET.fromstring(page.read().decode())

    # Create recipe object in database
    recipe = Recipe.objects.create(recipe_name=data.find('Title').text, bigoven_id=int(data.find('RecipeID').text))

    # For ingredient in recipe
    for i in data.iter('Ingredient'):
        # If the ingredient is a heading (ex. BRINE or AROMATICS)
        if i.find('IsHeading').text != 'true':
            # Set variables for ingredient
            name = i.find('Name').text
            try: # Not all are given units (ex. One Whole Chicken or 6 steaks)
                unit = i.find('Unit').text
            except:
                unit = 'None'
            quantity = i.find('Quantity').text

            # Create Ingredient object in database
            Ingredient.objects.create(
                recipe=recipe,
                name=name,
                unit=unit,
                amount=quantity
            )


sync_all(1, 3)
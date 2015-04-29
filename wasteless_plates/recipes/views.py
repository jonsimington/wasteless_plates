from django.shortcuts import render_to_response
from wasteless_plates.recipes.models import Recipe, Ingredient
import random


def results(request):
    # We're getting from the index page
    if request.method == 'GET':
        # This is the string that the user has entered
        user_query = request.GET['q']

        # The ingredients in the original query split by the commas
        ingredients = user_query.split(',')

        # Initialize the list and cycle through recipe objects filtering for ingredients
        all_recipes = list()

        # For every ingredient, we create a set in the list all_recipes including the ingredients used
        for i in range(len(ingredients)):
            # We use contains here because naming conventions from BigOven are not standardized
            all_recipes.append(set(Recipe.objects.filter(ingredient__item__name__contains=ingredients[i])))

        # This is where we actually use the intersections
        if len(ingredients) > 1:
            for i in range(len(ingredients) - 1):
                all_recipes[0] = all_recipes[i].intersection(all_recipes[i+1])

        # Return the response
        return render_to_response('recipes.html', {
            'recipes': all_recipes[0]
        })
    # Should never get here but if it does, returned that they failed.
    # (This will be apparent if they access url directly)
    return render_to_response('recipes.html', {
        'recipes': Recipe.objects.filter(ingredient__item__name__contains='FAILED')
    })


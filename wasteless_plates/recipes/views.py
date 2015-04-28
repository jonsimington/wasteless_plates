from django.shortcuts import render_to_response
from wasteless_plates.recipes.models import Recipe

def results(request):
    # We're getting from the index page
    if request.method == 'GET':
        # This is the string that the user has entered
        user_query = request.GET['q']

        # The ingredients in the original query split by the commas
        ingredients = user_query.split(',')

        # Initialize the list and cycle through recipe objects filtering for ingredients
        all_recipes = list()
        for i in ingredients:
            # We use contains here because naming conventions from BigOven are not standardized
            all_recipes += Recipe.objects.filter(ingredient__item__name__contains=i)

        # This is where we remove duplicates.
        all_recipes = list(set(all_recipes))

        # Return the response
        return render_to_response('recipes.html', {
            'recipes': all_recipes
        })

    # Should never get here but if it does, returned that they failed.
    # (This will be apparent if they access url directly)
    return render_to_response('recipes.html', {
        'recipes': Recipe.objects.filter(ingredient__item__name__contains='FAILED')
    })

"""
def recipeResult(request):
    #We're getting from the index page
    if request.method == 'GET':
        #The string the user entered
        user_query = request.GET['recipeQuery']

        all_recipes = list()
        for i in user_query:
            all_recipes += Recipe.objects.filter(recipe_name__contains=user_query)

        all_recipes = list(set(all_recipes))


        return render_to_response('recipes.html', {
            'validRecipes': all_recipes

        })
"""

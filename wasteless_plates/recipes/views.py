from django.shortcuts import render_to_response
from wasteless_plates.recipes.models import Recipe


def results(request):
    # We're getting from the index page
    if request.method == 'GET':
        # This is the string that the user has entered
        user_query = request.GET['q']

        # The ingredients in the original query split by the commas
        ingredients = user_query.split(',')

        recipe_set = set(Recipe.objects.filter(ingredient__item__name__contains=ingredients[0]))

        # For every ingredient, we create a set in the list all_recipes including the ingredients used
        for i in ingredients:
            i = i.lstrip().rstrip()
            # We use contains here because naming conventions from BigOven are not standardized
            print(i)
            temp = set(Recipe.objects.filter(ingredient__item__name__contains=i))
            print(temp)
            recipe_set = recipe_set.intersection(temp)

        # Return the response
        return render_to_response('recipes.html', {
            'recipes': recipe_set
        })

    # Should never get here but if it does, returned that they failed.
    # (This will be apparent if they access url directly)
    return render_to_response('recipes.html', {
        'recipes': Recipe.objects.filter(ingredient__item__name__contains='FAILED')
    })
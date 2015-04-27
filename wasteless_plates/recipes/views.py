from django.shortcuts import render_to_response
from wasteless_plates.recipes.models import Recipe

# Create your views here.
"""
def SearchView(request):
    #get the string after'q=' in url -> commma seperated list of ingredients
    query = request.GET.get('q')

    #redirect to the results page
    if query:
        return HttpResponseRedirect("/search/results/" + query)
    #else its invalid and send back to search bar
    else:
        return HttpResponseRedirect("/")


class SearchResultsView(TemplateView):
    #get string from kwargs
    query = self.kwargs['query']

    #get rid of the commas
    ingredients = [x.strip() for x in query.split(',')]

    shit_list = list()

    for i in ingredients:
        shit_list += Recipe.objects.filter(ingredient__item__exact='ingredients').filter()

    validRecipes=Recipe.objects.filter(ingredient__item__exact='ingredients')

    context = list()

    context = validRecipes

    return context
"""


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

        # This is where we remove duplicates. This was my fault on the db end.
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
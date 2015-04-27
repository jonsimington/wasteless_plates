from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from wasteless_plates.recipes.models import Recipe
from django.views.generic.base import TemplateView
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
    return render_to_response('recipes.html', {
        'recipes': Recipe.objects.filter(ingredient__item__name__contains='Garbage')
    })
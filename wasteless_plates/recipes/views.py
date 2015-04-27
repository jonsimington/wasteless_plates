from django.shortcuts import render

# Create your views here.
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
    template_name="recipes/recipes.html"

    #get string from kwargs
    query = self.kwargs['query']

    #get rid of the commas
    ingredients = [x.strip() for x in query.split(',')]

    validRecipes=Recipe.objects.filter(ingredient__item__exact'ingredients')

    context['recipes'] = validRecipes

    return context

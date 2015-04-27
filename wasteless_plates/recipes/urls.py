from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    #The page with all the recipes

    #url(r'^search/$','wasteless_plates.home.views.SearchView',name='search_recipes'),

    #url(r'^search/results/(?P<query>[/w-]+)/$', SearchResultsView.as_view(), name="search_results")
    url(
        r'^results/$',
        'wasteless_plates.recipes.views.results'
    )
)

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    #The page with all the recipes

    url(
        r'^results/$',
        'wasteless_plates.recipes.views.results'
    )

    #for the recipe search
#    url(
#        r'^recipeResult/$',
#        'wasteless_plates.recipes.views.recipeResult'
#    )
)

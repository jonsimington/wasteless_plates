from django.views.generic import TemplateView

# View for /
class HomePageView(TemplateView):
    template_name = "home/home.html"


class MinListView(TemplateView):
    validRecipes = Recipe.objects.filter(ingredient__item__exact())
    

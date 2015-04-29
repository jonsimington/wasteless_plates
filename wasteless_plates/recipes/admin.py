from django.contrib import admin

from wasteless_plates.recipes.models import Recipe, Ingredient, Nutrition, Item
 
class RecipeInline(admin.TabularInline):
    model = Recipe
    fields = ("recipe_name", "bigoven_id", "nutrition_info")

class IngredientInline(admin.TabularInline):
    model = Ingredient
    fields = ("recipe", "item")

class NutritionInline(admin.TabularInline):
    model = Nutrition
    fields = ("calories", "total_fat", "sodium", "sugar", "protein")

class ItemInline(admin.TabularInline):
    model = Item
    fields = ("name")
   
##########################################################################

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("recipe_name", "serving_size", "bigoven_id", "nutrition_info")
                    
    list_display_links = ("recipe_name", "nutrition_info")
    list_filter = ("recipe_name", "bigoven_id")
    search_fields = ("recipe_name",)

class IngredientAdmin(admin.ModelAdmin):
    list_display = ("recipe", "item", "unit", "amount")
                    
    list_display_links = ("recipe", "item")
    list_filter = ("recipe",)
    search_fields = ("recipe",)


class NutritionAdmin(admin.ModelAdmin):
    list_display = ("calories", "total_fat", "sodium", "protein", "sugar")
                    
    list_filter = ("calories", "total_fat", "sugar")


class ItemAdmin(admin.ModelAdmin):
    list_display = ("name",)
                    
    list_filter = ("name",)
    search_fields = ("name",)
    
################################################################################
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Nutrition, NutritionAdmin)
admin.site.register(Item, ItemAdmin)

from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import HomePage, Recipe, Ingredient, Instruction

# Unregister Group if needed
admin.site.unregister(Group)

# Customize admin site headers
admin.site.site_header = "Westbrook Recipes Admin"
admin.site.site_title = "Westbrook Recipes"
admin.site.index_title = "Welcome to Westbrook Recipes"

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'background_image')

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    exclude = ('ingredients',)  # ingredients field removed
    list_display = ('title', 'meal_type', 'display_favorites')
    list_filter = ('meal_type',)
    # Only include favorites in the horizontal filter
    filter_horizontal = ('favorites',)

    def display_favorites(self, obj):
        return ", ".join([user.username for user in obj.favorites.all()])
    display_favorites.short_description = 'Favorites'

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Instruction)
class InstructionAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

from django.contrib import admin

from .models import (Favorite, Ingredient, IngredientRecipe, Recipe, Tag,
                     TagRecipe)

EMPTY = '-пусто-'


class IngredientsInLine(admin.StackedInline):
    model = IngredientRecipe


class TagsInLine(admin.StackedInline):
    model = TagRecipe


class IngredientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'measurement_unit']
    search_fields = ['name']
    empty_value_display = EMPTY


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
    search_fields = ['name']


class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'text',
        'cooking_time',
        'favorites',
        'author'
    ]
    search_fields = ['name', 'text']
    list_filter = ['tags', 'author__username']
    empty_value_display = EMPTY
    inlines = [IngredientsInLine, TagsInLine]

    def favorites(self, obj):
        if Favorite.objects.filter(recipe=obj).exists():
            return Favorite.objects.filter(recipe=obj).count()
        return EMPTY


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)

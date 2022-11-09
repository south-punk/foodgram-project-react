from django.contrib import admin

from .models import Ingredient, Recipe, Tag


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'text',
        'cooking_time'
    )
    search_fields = ('name', 'text',)
    # filter_horizontal = ['ingredients', 'tags']


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)

"""Модуль конфигурации админ-панели проекта."""
from django.contrib import admin

from .models import (Favorite, Ingredient, IngredientRecipe, Recipe, Tag,
                     TagRecipe)

EMPTY = '-пусто-'


class IngredientsInLine(admin.StackedInline):
    """Класс отображения модели связанных рецепта и ингредиентов."""

    model = IngredientRecipe


class TagsInLine(admin.StackedInline):
    """Класс отображения модели связанных рецепта и тегов."""

    model = TagRecipe


class IngredientAdmin(admin.ModelAdmin):
    """Класс отображения модели ингредиента."""

    list_display = ['id', 'name', 'measurement_unit']
    search_fields = ['name']
    empty_value_display = EMPTY


class TagAdmin(admin.ModelAdmin):
    """Класс отображения модели тега."""

    list_display = ('name', 'color', 'slug')
    search_fields = ['name']


class RecipeAdmin(admin.ModelAdmin):
    """Класс отображения модели рецепта."""

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
        """Метод получения поля избранных рецептов."""
        if Favorite.objects.filter(recipe=obj).exists():
            return Favorite.objects.filter(recipe=obj).count()
        return EMPTY


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)

"""Модуль кастомных фильтров."""
from django_filters import rest_framework as filters
from recipes.models import Recipe, Tag
from rest_framework.filters import SearchFilter


class FilterRecipe(filters.FilterSet):
    """Кастомный фильтр для рецептов."""

    author = filters.CharFilter()
    tags = filters.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        queryset=Tag.objects.all(),
        label='Tags',
        to_field_name='slug'
    )
    is_favorited = filters.BooleanFilter(method='get_favorite')
    is_in_shopping_cart = filters.BooleanFilter(
        method='get_is_in_shopping_cart'
    )

    class Meta:
        """Внутренний класс для определения модели и полей для фильтрации."""

        model = Recipe
        fields = ['tags', 'author', 'is_favorited', 'is_in_shopping_cart']

    def get_favorite(self, queryset, name, value):
        """Поле избранного."""
        if value:
            return queryset.filter(favorites__user=self.request.user)
        return queryset

    def get_is_in_shopping_cart(self, queryset, name, value):
        """Поле корзины покупки."""
        if value:
            return queryset.filter(shopping_cart__user=self.request.user)
        return queryset


class IngredientSearchFilter(SearchFilter):
    """Кастомный поиск ингридиентов."""

    search_param = 'name'

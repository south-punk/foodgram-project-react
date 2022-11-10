from rest_framework import viewsets
from .serializers import (
    GetRecipeSerializer,
    IngredientSerializer,
    PostRecipeSerializer,
    TagSerializer
)
from recipes.models import (
    Ingredient,
    Recipe,
    Tag
)


class RecipeViewSet(viewsets.ModelViewSet):
    """ Представление рецептов."""

    queryset = Recipe.objects.all()
    serializer_class = PostRecipeSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetRecipeSerializer
        return PostRecipeSerializer


class TagViewSet(viewsets.ModelViewSet):
# class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """ Представление тегов."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IngredientViewSet(viewsets.ModelViewSet):
# class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    """ Представление ингредиентов."""

    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()

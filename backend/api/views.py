"""Модуль представлений приложения API."""
from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.http import HttpResponse
from django_filters import rest_framework as filters
from recipes.models import (Favorite, Ingredient, IngredientRecipe, Recipe,
                            ShoppingCart, Subscription, Tag)
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView

from .filters import FilterRecipe, IngredientSearchFilter
from .permissions import AdminOrReadOnly, AuthorOrAdminOrReadOnly
from .serializers import (FavoriteSerializer, IngredientSerializer,
                          RecipeCreateSerializer, RecipeListSerializer,
                          ShoppingCartSerializer,
                          SubscribeCreateDestroySerializer,
                          SubscribeListSerializer, TagSerializer)
from .utils import delete_object, post_object

User = get_user_model()


class RecipeViewSet(viewsets.ModelViewSet):
    """Представление рецептов."""

    queryset = Recipe.objects.all()
    permission_classes = (AuthorOrAdminOrReadOnly, )
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FilterRecipe

    def get_serializer_class(self):
        """Выбор сериализатора для обработки данных."""
        if self.request.method == 'GET':
            return RecipeListSerializer
        return RecipeCreateSerializer

    def perform_create(self, serializer):
        """Переопределение метода создания рецепта."""
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['GET'])
    def download_shopping_cart(self, request):
        """Метод для скачивания списка покупок."""
        ingredients = IngredientRecipe.objects.filter(
            recipe__shopping_cart__user=request.user
        ).values(
            'ingredient__name', 'ingredient__measurement_unit'
        ).annotate(sum=Sum('amount'))
        shopping_list = "Купить в магазине:"
        for ingredient in ingredients:
            shopping_list += (
                f"\n{ingredient['ingredient__name']} "
                f"({ingredient['ingredient__measurement_unit']}) - "
                f"{ingredient['sum']}")
        file = 'shopping_list.txt'
        response = HttpResponse(shopping_list, content_type='text/plain')
        response['Content-Disposition'] = f'attachment; filename="{file}.txt"'
        return response


class TagViewSet(viewsets.ModelViewSet):
    """Представление тегов."""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AdminOrReadOnly, )
    pagination_class = None


class IngredientViewSet(viewsets.ModelViewSet):
    """Представление ингредиентов."""

    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    permission_classes = (AdminOrReadOnly, )
    filter_backends = (IngredientSearchFilter, )
    search_fields = ['^name']
    pagination_class = None


class SubscribeListView(generics.ListAPIView):
    """Представление вывода подписок."""

    def get(self, request):
        """Метод получения списка подписок."""
        user = request.user
        queryset = User.objects.filter(following__user=user)
        page = self.paginate_queryset(queryset)
        serializer = SubscribeListSerializer(
            page,
            many=True,
            context={'request': request}
        )
        return self.get_paginated_response(serializer.data)


class SubscribeCreateDestroyView(APIView):
    """Представление создания подписок."""

    def post(self, request, id):
        """Метод создания подписки."""
        return post_object(SubscribeCreateDestroySerializer, request, id)

    def delete(self, request, id):
        """Метод удаления подписки."""
        return delete_object(User, Subscription, request, id)


class FavoriteView(APIView):
    """Представление избранного."""

    def post(self, request, id):
        """Метод добавления рецепта в список избранного."""
        return post_object(FavoriteSerializer, request, id)

    def delete(self, request, id):
        """Метод удаления рецепта из списка избранного."""
        return delete_object(Recipe, Favorite, request, id)


class ShoppingCartView(APIView):
    """Представление списка покупок."""

    def post(self, request, id):
        """Метод добавления рецепта в список покупок."""
        return post_object(ShoppingCartSerializer, request, id)

    def delete(self, request, id):
        """Метод удаления рецепта из списка покупок."""
        return delete_object(Recipe, ShoppingCart, request, id)

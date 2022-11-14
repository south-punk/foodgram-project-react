from rest_framework import viewsets
from .serializers import (
    FavoriteSerializer,
    IngredientSerializer,
    RecipeCreateSerializer,
    RecipeListSerializer,
    ShoppingCartSerializer,
    SubscribeCreateDestroySerializer,
    SubscribeListSerializer,
    TagSerializer
)
from recipes.models import (
    Favorite,
    Ingredient,
    IngredientRecipe,
    Recipe,
    Subscription,
    ShoppingCart,
    Tag
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Sum
from rest_framework.decorators import action
from django.http import HttpResponse

User = get_user_model()


class RecipeViewSet(viewsets.ModelViewSet):
    """ Представление рецептов."""

    queryset = Recipe.objects.all()
    serializer_class = RecipeCreateSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RecipeListSerializer
        return RecipeCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['GET'])
    def download_shopping_cart(self, request):
        ingredients = IngredientRecipe.objects.filter(
            recipe__shopping_cart__user=request.user
        ).values(
            'ingredient__name', 'ingredient__measurement_unit'
            ).annotate(amount=Sum('amount'))
        shopping_list = "Купить в магазине:"
        for ingredient in ingredients:
            shopping_list += (
                f"\n{ingredient['ingredient__name']} "
                f"({ingredient['ingredient__measurement_unit']}) - "
                f"{ingredient['amount']}")
        file = 'shopping_list.txt'
        response = HttpResponse(shopping_list, content_type='text/plain')
        response['Content-Disposition'] = f'attachment; filename="{file}.txt"'
        return response


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


class SubscribeListView(generics.ListAPIView):
    """Представление вывода подписок."""

    def get(self, request):
        user = request.user
        queryset = User.objects.filter(following__user=user)
        serializer = SubscribeListSerializer(
            queryset,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubscribeCreateDestroyView(APIView):
    """Представление создания подписок."""

    def post(self, request, id):
        serializer = SubscribeCreateDestroySerializer(
            data={
                'user': request.user.id,
                'author': id
                },
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        author = get_object_or_404(User, id=id)
        subscribe = Subscription.objects.filter(user=request.user.id,
                                                author=author)
        if subscribe.exists():
            subscribe.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


class FavoriteView(APIView):
    """Представление избранного."""

    def post(self, request, id):
        serializer = FavoriteSerializer(
            data={
                'user': request.user.id,
                'recipe': id
                },
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
        favorite = Favorite.objects.filter(user=request.user.id,
                                           recipe=recipe)
        if favorite.exists():
            favorite.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


class ShoppingCartView(APIView):
    """Представление списка покупок."""

    def post(self, request, id):
        serializer = ShoppingCartSerializer(
            data={
                'user': request.user.id,
                'recipe': id
                },
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
        favorite = ShoppingCart.objects.filter(user=request.user.id,
                                               recipe=recipe)
        if favorite.exists():
            favorite.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

from rest_framework import viewsets
from .serializers import (
    FavoriteCreateDestroySerializer,
    IngredientSerializer,
    RecipeCreateSerializer,
    RecipeListSerializer,
    SubscribeCreateDestroySerializer,
    SubscribeListSerializer,
    TagSerializer
)
from recipes.models import (
    Favorite,
    Ingredient,
    Recipe,
    Subscription,
    Tag
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

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
    """ Отображение подписок. """

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


class FavoriteCreateDestroyView(APIView):

    def post(self, request, id):
        serializer = FavoriteCreateDestroySerializer(
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

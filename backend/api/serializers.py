from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from recipes.models import (
    Favorite,
    Ingredient,
    IngredientRecipe,
    Recipe,
    Subscription,
    ShoppingCart,
    Tag,
    TagRecipe
)
from rest_framework.validators import UniqueTogetherValidator


User = get_user_model()


class CustomUserSerializer(UserSerializer):
    """Сериализатор пользователя/ей."""
    class Meta:
        model = User
        fields = [
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
        ]


class CustomUserCreateSerializer(UserCreateSerializer):
    """Сериализатор создания пользователя."""

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
            'password'
        ]


class TagSerializer(serializers.ModelSerializer):
    """Сериализатор для тегов."""

    class Meta:
        model = Tag
        fields = ['id', 'name', 'color', 'slug']


class IngredientSerializer(serializers.ModelSerializer):
    """Сериализатор для Ингредиентов."""

    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'measurement_unit']


class RecipeIngredientSerializer(serializers.ModelSerializer):
    """Сериализатор модели, связывающей ингредиенты и рецепт."""

    id = serializers.ReadOnlyField(source='ingredient.id')
    name = serializers.ReadOnlyField(source='ingredient.name')
    measurement_unit = serializers.ReadOnlyField(
        source='ingredient.measurement_unit'
    )

    class Meta:
        model = IngredientRecipe
        fields = ['id', 'name', 'amount', 'measurement_unit']


class AmountIngredientInRecipeSerializer(serializers.ModelSerializer):
    """Сериализатор добавления ингредиента (с количеством) в рецепт."""

    id = serializers.IntegerField()

    class Meta:
        model = IngredientRecipe
        fields = ['id', 'amount']


class RecipeListSerializer(serializers.ModelSerializer):
    """Сериализатор для получения рецепта(-ов)."""

    tags = TagSerializer(read_only=True, many=True)
    ingredients = serializers.SerializerMethodField()
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Recipe
        fields = [
            'id',
            'tags',
            'author',
            'ingredients',
            # 'is_favorited',
            # 'is_in_shopping_cart'
            'name',
            # 'image',
            'text',
            'cooking_time',
        ]

    def get_ingredients(self, obj):
        ingredients = IngredientRecipe.objects.filter(recipe=obj)
        return RecipeIngredientSerializer(ingredients, many=True).data


class RecipeListSubscribeSerializer(serializers.ModelSerializer):
    """Вывод рецептов в подписках пользователя."""

    class Meta:
        model = Recipe
        fields = [
            'id',
            'name',
            # 'image',
            'cooking_time',
        ]


class RecipeCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания/обновления/удаления рецепта(-ов)."""

    ingredients = AmountIngredientInRecipeSerializer(many=True)
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True
    )

    class Meta:
        model = Recipe
        fields = [
            'ingredients',
            'tags',
            # 'image',
            'name',
            'text',
            'cooking_time',
            # 'author'
        ]
        read_only_fields = ['author']

    def create(self, validated_data):
        """Создание рецепта."""

        ingredients = validated_data.pop('ingredients')
        tags = validated_data.pop('tags')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient in ingredients:
            current_ingredient = Ingredient.objects.get(id=ingredient['id'])
            IngredientRecipe.objects.create(
                ingredient=current_ingredient,
                recipe=recipe,
                amount=ingredient['amount']
            )
        for tag in tags:
            TagRecipe.objects.create(recipe=recipe, tag=tag)
        return recipe

    def to_representation(self, recipe):
        return RecipeListSerializer(recipe, context=self.context).data


class SubscribeListSerializer(serializers.ModelSerializer):
    """Сериализатор для получения подписок"""

    is_subscribed = serializers.SerializerMethodField()
    recipes = RecipeListSubscribeSerializer(read_only=True, many=True)
    recipes_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'is_subscribed',
            'recipes',
            'recipes_count'
        ]

    def get_is_subscribed(self, obj):
        request = self.context['request']
        if Subscription.objects.filter(user=request.user, author=obj).exists():
            return True
        return False

    def get_recipes_count(self, obj):
        return Recipe.objects.filter(author=obj).count()


class SubscribeCreateDestroySerializer(serializers.ModelSerializer):
    """Сериализатор для создания/удаления подписки."""

    class Meta:
        model = Subscription
        fields = ['user', 'author']
        validators = [
            UniqueTogetherValidator(
                queryset=Subscription.objects.all(),
                fields=['user', 'author'],
                message='Подписка уже существует!'
            )
        ]

    def to_representation(self, instance):
        return SubscribeListSerializer(instance.author,
                                       context=self.context).data


class FavoriteSerializer(serializers.ModelSerializer):
    """Сериализатор для избранного."""

    class Meta:
        model = Favorite
        fields = ['user', 'recipe']
        validators = [
            UniqueTogetherValidator(
                queryset=Favorite.objects.all(),
                fields=['user', 'recipe'],
                message='Рецепт уже добавлен в список избранного'
            )
        ]

    def to_representation(self, instance):
        return RecipeListSubscribeSerializer(instance.recipe,
                                             context=self.context).data


class ShoppingCartSerializer(serializers.ModelSerializer):
    """Сериализатор для списка покупок."""

    class Meta:
        model = ShoppingCart
        fields = ['user', 'recipe']
        validators = [
            UniqueTogetherValidator(
                queryset=ShoppingCart.objects.all(),
                fields=['user', 'recipe'],
                message='Рецепт уже добавлен в список покупок'
            )
        ]

    def to_representation(self, instance):
        return RecipeListSubscribeSerializer(instance.recipe,
                                             context=self.context).data

from rest_framework import serializers
from recipes.models import Recipe, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'name',
            'color',
            'slug'
        ]


class RecipeSerializer(serializers.ModelSerializer):
    tag = serializers.SlugRelatedField(
        slug_field="id", many=True, queryset=Tag.objects.all()
    )

    class Meta:
        model = Recipe
        fields = [
            'id',
            'name',
            'text',
            'cooking_time',
            'tag'
        ]

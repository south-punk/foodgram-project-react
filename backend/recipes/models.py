from django.db import models
from django.core.validators import MinValueValidator

MIN_COOKING_TIME = 1


class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название тега')
    color = models.CharField(max_length=7, verbose_name='Цвет тега в HEX')
    slug = models.SlugField(max_length=200, unique=True,
                            verbose_name='Слаг тега')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Теги'
        verbose_name_plural = 'Теги'


class Recipe(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    text = models.TextField(verbose_name='Описание')
    cooking_time = models.IntegerField(
        validators=[MinValueValidator(MIN_COOKING_TIME)],
        verbose_name='Время приготовления')
    tag = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='теги'
        )
    """
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientRecipe',
        related_name='ingredients',
        verbose_name='ингридиенты'
        )
    tags = models.ManyToManyField(
        Tag,
        # on_delete=models.DO_NOTHING,
        related_name='tags',
        verbose_name='теги'
        )
    image = models.ImageField(
        upload_to='img/',  # настроить папку!
        null=True,
        default=None
        )
    """

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Рецепты'
        verbose_name_plural = 'Рецепты'

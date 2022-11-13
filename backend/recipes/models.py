from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model

MIN = 1

User = get_user_model()


class Ingredient(models.Model):
    """ Модель ингредиентов для рецептов."""

    name = models.CharField(max_length=200,
                            verbose_name='Название ингридиента')
    measurement_unit = models.CharField(max_length=200,
                                        verbose_name='Единицы измерения')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Ингридиенты'
        verbose_name_plural = 'Ингридиенты'


class Tag(models.Model):
    """ Модель тэгов для рецептов."""

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
    """ Модель рецептов."""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор рецепта'
    )
    name = models.CharField(max_length=200, verbose_name='Название')
    text = models.TextField(verbose_name='Описание')
    cooking_time = models.IntegerField(
        validators=[MinValueValidator(MIN)],
        verbose_name='Время приготовления')
    tags = models.ManyToManyField(
        Tag,
        through='TagRecipe',
        related_name='recipes',
        verbose_name='теги'
        )

    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientRecipe',
        related_name='recipes',
        verbose_name='ингридиенты'
    )
    """
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


class TagRecipe(models.Model):
    """ Модель связи рецепта и тега."""

    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tag} - {self.recipe}'


class IngredientRecipe(models.Model):
    """ Модель связи рецепта и ингридиента с количеством."""

    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    amount = models.IntegerField(validators=[MinValueValidator(MIN)],
                                 verbose_name='Количество')

    def __str__(self):
        return f'{self.recipe} - {self.ingredient} {self.amount}'


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор рецептов'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_user_author'
            )
        ]

    def __str__(self):
        return f'подписка пользователя {self.user} на {self.author}'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='users',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favotites',
        verbose_name='Избранный рецепт'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_user_recipe'
            )
        ]

    def __str__(self):
        return f'{self.recipe} добавлен в избранное пользователя {self.user}'

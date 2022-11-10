from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class User(AbstractUser):
    """Модель пользователей."""

    # username = models.CharField(
    #     max_length=150,
    #     unique=True,
    #     validators=[UnicodeUsernameValidator()],
    #     verbose_name='Логин'
    # )
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Адрес электронной почты'
    )
    first_name = models.TextField(max_length=150, verbose_name='Имя')
    last_name = models.TextField(max_length=150, verbose_name='Фамилия')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

"""Модуль описания моделей проекта."""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователей."""

    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Адрес электронной почты'
    )
    first_name = models.TextField(max_length=150, verbose_name='Имя')
    last_name = models.TextField(max_length=150, verbose_name='Фамилия')

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    class Meta:
        """Внутренний класс конфигурации модели."""

        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        """Метод представления объектов."""
        return self.username

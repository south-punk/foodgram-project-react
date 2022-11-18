"""Модуль конфигурации админ-панели проекта."""
from django.contrib import admin

from .models import User

EMPTY = '-пусто-'


class UserAdmin(admin.ModelAdmin):
    """Класс отображения модели пользователя."""

    list_display = ['username', 'email', 'first_name', 'last_name']
    search_fields = ['username', 'email']
    list_filter = ['first_name', 'last_name']
    ordering = ['username']
    empty_value_display = EMPTY


admin.site.register(User, UserAdmin)

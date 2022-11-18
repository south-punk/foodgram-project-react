"""Модуль проверки права доступа."""
from rest_framework import permissions


class AuthorOrAdminOrReadOnly(permissions.BasePermission):
    """Доступ разрешен тольк автору или админу, остальным только чтение."""

    def has_object_permission(self, request, view, obj):
        """Права на уровне запроса и пользователя."""
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user or request.user.is_staff)


class AdminOrReadOnly(permissions.BasePermission):
    """Доступ разрешен только админу, остальным только чтение."""

    def has_permission(self, request, view):
        """Права на уровне объекта."""
        if request.user.is_authenticated:
            return (request.user.is_staff
                    or request.method in permissions.SAFE_METHODS)
        return request.method in permissions.SAFE_METHODS

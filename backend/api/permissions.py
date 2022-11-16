from rest_framework import permissions


class AuthorOrAdminOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user or request.user.is_staff)


class AdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return (request.user.is_staff
                    or request.method in permissions.SAFE_METHODS)
        else:
            return request.method in permissions.SAFE_METHODS

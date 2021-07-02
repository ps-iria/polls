from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS
)


class IsAdmin(BasePermission):
    """Проверка что пользователь является админом"""
    def has_permission(self, request, view):
        return (request.user.is_staff or
                request.user.is_superuser or
                request.user.is_admin)


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return request.user.is_staff or request.user.is_admin

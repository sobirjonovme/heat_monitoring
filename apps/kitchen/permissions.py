from rest_framework.permissions import BasePermission


class IsCookOrAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (user.is_cook() or user.is_admin())


class IsProvider(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.is_provider()

from rest_framework.permissions import BasePermission


class IsFarmCounterOrAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (user.is_farm_counter() or user.is_admin())

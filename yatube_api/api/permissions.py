from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS
)


class IsAuthorOrReadOnly(BasePermission):
    """Класс разрешений, позволяющий редактировать контент только автору."""

    def has_object_permission(self, request, view, obj):
        """Check if user has permission to modify object.

        Returns True if request is safe
        (GET, HEAD, OPTIONS) or if user is author.
        """
        return request.method in SAFE_METHODS or obj.author == request.user

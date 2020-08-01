from rest_framework import permissions


class IsSuperUser(permissions.IsAdminUser):
    # Superusers only permission
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permission for anyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permission for the recipe author (or a superuser, see)
        return obj.author == request.user

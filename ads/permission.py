from rest_framework import permissions
from user.models import Author


class SelectionPermissions(permissions.BasePermission):
    message = "Create or Update or Delete selection for non author not allowed"

    def has_permission(self, request, view):
        if request.author.pk == Author.pk:
            return True
        return False


class AdminOrModeratorPermissions(permissions.BasePermission):
    message = "Update or Delete announcement for non admin or moderator not allowed"

    def has_permission(self, request, view):
        if request.author.role == Author.role:
            return True
        return False

from rest_framework import permissions
from user.models import Author


class CheckUserPermissions(permissions.BasePermission):
    message = "Create or Update or Delete selection for non author not allowed"

    def has_object_permission(self, request, view, obj):
        if request.author == obj.author:
            return True
        return False


class AdminOrModeratorPermissions(permissions.BasePermission):
    message = "Update or Delete announcement for non admin or moderator not allowed"

    def has_permission(self, request, view):
        if request.author.role == 'admin' or request.author.role == 'moderator':
            return True
        return False

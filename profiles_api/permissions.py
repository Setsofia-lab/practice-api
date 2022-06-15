from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit own profile"""

    def has_objects_permissions(self, request,view, obj):
        """Check if user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return object.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to updat ewon status"""

    def has_object_permission(self, request, view, obj):
        """Check the userr is trying to update their own staus"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
from rest_framework.permissions import BasePermission


class IsThisUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.id


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user

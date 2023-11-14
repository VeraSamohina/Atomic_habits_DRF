from rest_framework.permissions import BasePermission, SAFE_METHODS


# class IsOwnerOrReadOnly(BasePermission):
#
#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
#         return obj.pk == request.user.pk


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.id

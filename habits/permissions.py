from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "Вы можете работать только со своими привычками"

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
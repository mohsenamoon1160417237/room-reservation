from rest_framework.permissions import BasePermission



class IsManager(BasePermission):

    message = 'You are not a manager'

    def has_permission(self, request, view):

        user = request.user
        return user.user_type == 'manager'

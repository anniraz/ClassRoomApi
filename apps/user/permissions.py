from rest_framework import permissions


class IsOwn(permissions.BasePermission):
    '''
    permission for own verification
    '''
    def has_object_permission(self, request, view, obj):
        return bool(obj == request.user)
from rest_framework import permissions


class IsCourseOwner(permissions.BasePermission):
    '''
    permission for owner verification
    '''
    def has_object_permission(self, request, view, obj):
        return bool(obj.owner == request.user)
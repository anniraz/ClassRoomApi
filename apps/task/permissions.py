from rest_framework import permissions

from apps.courses.models import CourseMembers


class IsTaskOwner(permissions.BasePermission):
    '''
    permission for task owner verification
    '''
    def has_object_permission(self, request, view, obj):
        return bool(obj.course.owner == request.user)


class IsTaskAttachOwner(permissions.BasePermission):
    '''
    permission for (attach to task) task  owner verification
    '''
    def has_object_permission(self, request, view, obj):
        return bool(obj.task.course.owner == request.user)


class HomeworksPermission(permissions.BasePermission):
    ''' 
    homework owner permission
    '''
    def has_object_permission(self, request, view, obj):
        return bool(obj.user == request.user)


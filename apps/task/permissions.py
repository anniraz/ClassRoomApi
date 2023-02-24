from rest_framework import permissions

from apps.courses.models import CourseMembers,Courses


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


class IsTeacher(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        members=[i.user for i in CourseMembers.objects.filter(course=obj.task.course) if i.is_teacher==True]
        return bool(request.user in members or request.user== obj.task.course.owner)
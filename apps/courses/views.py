from rest_framework import viewsets,permissions
from rest_framework.response import Response

from apps.courses.models import *
from apps.courses.serializers import *
from apps.courses.permissions import IsCourseOwner


class CourseApiView(viewsets.ModelViewSet):
    queryset=Courses.objects.all()
    serializer_class=CourseSerializers

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        my_courses=[i.course.id for i in CourseMembers.objects.filter(user=self.request.user)]
        return Courses.objects.filter(pk__in=my_courses)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy',]:
            return (IsCourseOwner(), )
        else:
            return (permissions.IsAuthenticated(),)  


class CourseMembersApiView(viewsets.ModelViewSet):
    queryset=CourseMembers.objects.all()
    serializer_class=CourseMemberSerializers

    def create(self, request, *args, **kwargs):
        course = request.data['course']
        if course.owner==request.user:
            return super().create(request,*args, **kwargs)
        return Response({"ERROR":"You are not the owner"})
            



    
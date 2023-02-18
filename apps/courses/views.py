from rest_framework import viewsets,permissions

from apps.courses.models import *
from apps.courses.serializers import *

class CourseApiView(viewsets.ModelViewSet):
    queryset=Courses.objects.all()
    serializer_class=CourseSerializers

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)



class CourseMembersApiView(viewsets.ModelViewSet):
    queryset=CourseMembers.objects.all()
    serializer_class=CourseMemberSerializers


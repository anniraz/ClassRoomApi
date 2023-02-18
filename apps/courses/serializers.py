from rest_framework import serializers
from apps.courses.models import Courses,CourseMembers


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields='__all__'
        read_only_fields=('id','owner',)



class CourseMemberSerializers(serializers.ModelSerializer):
    class Meta:
        model=CourseMembers
        fields='__all__'

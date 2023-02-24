from django.db.models import Q

from rest_framework import viewsets,permissions
from rest_framework.response import Response

from apps.task.models import Task,AttachToTask,Homeworks
from apps.task.serializers import TaskSerializers,AttachToTaskSerializers,HomeworksSerializers,HomeworkCheckTeacher
from apps.task.permissions import IsTaskOwner,IsTaskAttachOwner,HomeworksPermission,IsTeacher
from apps.courses.models import Courses,CourseMembers




class TaskApiViewSet(viewsets.ModelViewSet):
    
    queryset=Task.objects.all()
    serializer_class=TaskSerializers

    def get_queryset(self):
        my_courses=[i.course.id for i in CourseMembers.objects.filter(user=self.request.user)]
        return Task.objects.filter(Q(course__pk__in=my_courses)|Q(course__owner=self.request.user))


    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy',]:
            return (IsTaskOwner(), )
        else:
            return (permissions.IsAuthenticated(),)  

    def create(self, request, *args, **kwargs):
        course = request.data['course']
        owner=Courses.objects.get(id=course).owner
        if owner==request.user:
            return super().create(request,*args, **kwargs)
        return Response({"ERROR":"You are not the owner"})




class AttachToTaskApiViewSet(viewsets.ModelViewSet):

    queryset=AttachToTask.objects.all()
    serializer_class=AttachToTaskSerializers

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy',]:
            return (IsTaskAttachOwner(), )
        else:
            return (permissions.IsAuthenticated(),)  


    def create(self, request, *args, **kwargs):
        task = request.data['task']
        course_id=Task.objects.get(id=task).course.id
        owner=Courses.objects.get(id=course_id).owner
        if owner==request.user:
            return super().create(request,*args, **kwargs)
        return Response({"ERROR":"You are not the owner"}) 



class HomeworksApiView(viewsets.ModelViewSet):

    queryset=Homeworks.objects.all()
    serializer_class=HomeworksSerializers
    permission_classes=[HomeworksPermission]

    def get_queryset(self):
        return Homeworks.objects.filter(user=self.request.user)


    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
        

    def create(self, request, *args, **kwargs):
        task = request.data['task']
        course=Task.objects.get(id=task).course
        members=[i.user for i in CourseMembers.objects.filter(course=course)]

        if request.user in members:
            return super().create(request,*args, **kwargs)
        return Response({"ERROR":"You are not a student of this course"}) 
 



class HomeWorkCheckApiView(viewsets.ModelViewSet):
    queryset=Homeworks.objects.all()
    serializer_class=HomeworkCheckTeacher
    permission_classes=[IsTeacher]


from django.db.models import Q

from rest_framework import viewsets,permissions
from rest_framework.response import Response

from apps.task.models import Task,AttachToTask
from apps.task.serializers import TaskSerializers,AttachToTaskSerializers
from apps.task.permissions import IsTaskOwner,IsTaskAttachOwner
from apps.courses.models import Courses


class TaskApiViewSet(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=TaskSerializers

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


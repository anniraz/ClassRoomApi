from django.db.models import Q
from django.utils import timezone

from rest_framework import viewsets,permissions
from rest_framework.response import Response

from apps.task.models import Task,AttachToTask,Homeworks,Comment
from apps.task.serializers import TaskSerializers,AttachToTaskSerializers,HomeworksSerializers,HomeworkCheckTeacher,CommentSerializer
from apps.task.permissions import IsTaskOwner,IsTaskAttachOwner,HomeworksPermission,IsTeacher
from apps.courses.models import Courses,CourseMembers

from apps.task.tasks import send_comment,send_message




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
        task1=Task.objects.get(id=task)

        members=[i.user for i in CourseMembers.objects.filter(course=course)]

        if request.user in members:
            if (timezone.now() - task1.deadline)> timezone.timedelta(minutes=1):
                send_message.delay(request.user.email,request.user.username)
            return super().create(request,*args, **kwargs)


        return Response({"ERROR":"You are not a student of this course"}) 
 


class HomeWorkCheckApiView(viewsets.ModelViewSet):
    queryset=Homeworks.objects.all()
    serializer_class=HomeworkCheckTeacher
    permission_classes=[IsTeacher]



class CommentApiView(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


    def create(self, request, *args, **kwargs):
        hw_id=request.data['to_homework']
        text=request.data['text']
        homeworks=Homeworks.objects.get(id=hw_id)
        task=Task.objects.get(id=homeworks.task.id)
        course=Courses.objects.get(id=task.course.id)
        course_members=[i.user for i in CourseMembers.objects.filter(course=course) if i.is_teacher==True]

        if request.user in course_members or request.user==course.owner or request.user==homeworks.user:
            send_comment.delay(
                email=homeworks.user.email,
                username=request.user.username,
                text=text,
                to_user=homeworks.user.username
                )
            return super().create(request,*args, **kwargs)
        return Response({"ERROR":"You can't send message"}) 
    
    

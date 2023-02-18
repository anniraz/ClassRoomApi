from django.db import models
from django.contrib.auth import get_user_model
from apps.courses.models import Courses

User=get_user_model()


class Task(models.Model):
    course=models.ForeignKey(Courses, on_delete=models.CASCADE,related_name='course_task')
    title=models.CharField(max_length=255)
    instructions=models.TextField()
    points=models.PositiveIntegerField(default=100)
    subject=models.CharField(max_length=100,null=True,blank=True)
    deadline=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"{self.course}:{self.title}"


class AttachToTask(models.Model):
    task=models.ForeignKey(Task, on_delete=models.CASCADE,related_name='attach_task')
    link=models.CharField(max_length=1000,null=True,blank=True)
    image=models.ImageField(upload_to='task/',null=True,blank=True)
    files=models.FileField(upload_to='task/',null=True,blank=True)

    def __str__(self):
        return f"{self.task}"


class Homeworks(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    task=models.ForeignKey(Task, on_delete=models.CASCADE)
    link=models.CharField(max_length=1000,null=True,blank=True)
    image=models.ImageField(upload_to='homeworks/',null=True,blank=True)
    files=models.FileField(upload_to='homeworks/',null=True,blank=True)
    time_published=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.task}"
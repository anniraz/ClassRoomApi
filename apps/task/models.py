from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()


class Task(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    instructions=models.TextField()
    points=models.PositiveIntegerField(default=100)
    subject=models.CharField(max_length=100,null=True,blank=True)
    deadline=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"{self.owner}:{self.title}"


class AttachToTask(models.Model):
    task=models.ForeignKey(Task, on_delete=models.CASCADE)
    link=models.CharField(max_length=1000,null=True,blank=True)
    image=models.ImageField(upload_to='task/',null=True,blank=True)
    files=models.FileField(null=True,blank=True)

    def __str__(self):
        return f"{self.task}"
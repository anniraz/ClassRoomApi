from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()


class Courses(models.Model):

    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    audience=models.CharField(max_length=255,null=True,blank=True)
    chapter=models.CharField(max_length=255,null=True,blank=True)
    descriptions=models.TextField(null=True,blank=True)

    def __str__(self):
        return f'{self.owner}:{self.title}'


class CourseMembers(models.Model):
    is_teacher=models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    course=models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}:teacher:{self.is_teacher}-->{self.course}"
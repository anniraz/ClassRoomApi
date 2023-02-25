from django.contrib import admin
from apps.task.models import Task,AttachToTask,Homeworks,Comment

admin.site.register(Task)
admin.site.register(AttachToTask)
admin.site.register(Homeworks)
admin.site.register(Comment)
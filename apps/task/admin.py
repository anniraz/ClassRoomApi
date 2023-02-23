from django.contrib import admin
from apps.task.models import Task,AttachToTask,Homeworks

admin.site.register(Task)
admin.site.register(AttachToTask)
admin.site.register(Homeworks)
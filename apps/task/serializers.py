from rest_framework import serializers

from apps.task.models import Task,AttachToTask



class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'



class AttachToTaskSerializers(serializers.ModelSerializer):
    class Meta:
        model=AttachToTask
        fields='__all__'
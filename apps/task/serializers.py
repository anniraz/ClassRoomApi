from rest_framework import serializers

from apps.task.models import Task,AttachToTask,Homeworks



class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'


class AttachToTaskSerializers(serializers.ModelSerializer):
    class Meta:
        model=AttachToTask
        fields='__all__'


class HomeworksSerializers(serializers.ModelSerializer):
    class Meta:
        model=Homeworks
        fields='__all__'
        read_only_fields=('id','user','points',)
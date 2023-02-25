from rest_framework import serializers

from apps.task.models import Task,AttachToTask,Homeworks,Comment



class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'



class AttachToTaskSerializers(serializers.ModelSerializer):
    class Meta:
        model=AttachToTask
        fields='__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=('id','user','to_homework','text',)
        read_only_fields=('id','user',)



class HomeworksSerializers(serializers.ModelSerializer):
    homework_comment=CommentSerializer(many=True,read_only=True)
    class Meta:
        model=Homeworks   
        fields=['id','user','points','files','image','link','task','homework_comment']
        read_only_fields=('id','user','points',)


class HomeworkCheckTeacher(serializers.ModelSerializer):
     class Meta:
        model=Homeworks
        fields=('id','user','task','time_published','points',)
        read_only_fields=('id','user','time_published',)

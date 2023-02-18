from rest_framework import serializers

from apps.user.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id",
                  "email",
                  "username",
                  "first_name",
                  "last_name",
                  "avatar",
                  'password',

                  )

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
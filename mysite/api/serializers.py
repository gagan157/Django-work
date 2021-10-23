from rest_framework import serializers
from django.contrib.auth.models import User
from userdetails.models import UserProfile


#class model
class UserProfileSerliz(serializers.ModelSerializer):
    class META:
        model = UserProfile
        fields=['username','phone','Gender','Address','Country','State']



#create user 
class SignUpSerliz(serializers.Serializer):
    username = serializers.CharField(max_length=500)
    first_name = serializers.CharField(max_length=500)
    last_name = serializers.CharField(max_length=500)
    email = serializers.EmailField(max_length=500)
    password1 = serializers.CharField(max_length=500)
    password2 = serializers.CharField(max_length=500)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

#Get user and update user
class UserSerlize(serializers.Serializer):
    username = serializers.CharField(max_length=500)
    first_name = serializers.CharField(max_length=500)
    last_name = serializers.CharField(max_length=500)
    email = serializers.EmailField(max_length=500)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.email = validated_data.get('email',instance.email)
        instance.save()
        return instance



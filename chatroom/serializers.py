from rest_framework import serializers
from .models import Message, Conversation
from django.contrib.auth.models import User


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class ConversationSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Conversation
        fields = ('pk', 'host', 'title', 'desc', 'message_set')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('username', 'first_name', 'last_name', 'email', 'is_active',
        #           'is_staff', 'date_joined', 'last_login')
        exclude = ('password',)

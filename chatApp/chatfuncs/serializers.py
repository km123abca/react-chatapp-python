from rest_framework import serializers
from chatfuncs.models import *


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = chat
        fields = '__all__'


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = likes
        fields = '__all__'

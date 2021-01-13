from django.shortcuts import render

# Create your views here.
from chatfuncs.models import *
from rest_framework import viewsets, permissions
from chatfuncs.serializers import ChatSerializer, LikesSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = chat.objects.all()
    permission_classes = [
        permissions.AllowAny
        # permissions.IsAuthenticated
    ]

    serializer_class = ChatSerializer


class LikesViewSet(viewsets.ModelViewSet):
    # queryset = likes.objects.all()
    serializer_class = LikesSerializer
    permission_classes = [
        permissions.AllowAny
        # permissions.IsAuthenticated
    ]

    def get_queryset(self):
        parentchat = self.request.query_params.get('parentchat')
        qs = likes.objects.all()
        # if !parentchat:
        #     qs = likes.objects.all()
        # else:
        #     qs = likes.objects.filter(parentchat=parentchat)
        return qs

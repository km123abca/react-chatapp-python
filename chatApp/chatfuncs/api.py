from chatfuncs.models import *
from rest_framework import viewsets, permissions
from chatfuncs.serializers import ChatSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = chat.objects.all()
    permission_classes = [
        permissions.AllowAny
        # permissions.IsAuthenticated
    ]

    serializer_class = ChatSerializer


from .models import (Message, Conversation)
from .serializers import (ConversationSerializer, MessageSerializer, UserSerializer)
from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework import (status, mixins, generics, viewsets)
from rest_framework.decorators import (action)
from rest_framework.permissions import *
from rest_framework.response import Response

User = get_user_model()



class ConverstionViewSet(viewsets.ModelViewSet):
    """
    Viewset for Conversation model
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(['get'], detail=False)
    def identity(self, request):
        """
        returns the user details of the authenticated user
        """
        if request.user and request.user.is_authenticated:
            serializer = self.serializer_class(request.user)
            return Response(serializer.data)
        else:
            return Response({'details': 'not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)



class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
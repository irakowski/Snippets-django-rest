from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadonly

class SnippetList(generics.ListCreateAPIView):
    """
    Concrete view for listing a queryset or creating a model instance.
    #http://www.cdrf.co/3.9/rest_framework.generics/ListCreateAPIView.html
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadonly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance
    #http://www.cdrf.co/3.9/rest_framework.generics/RetrieveUpdateDestroyAPIView.html
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadonly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
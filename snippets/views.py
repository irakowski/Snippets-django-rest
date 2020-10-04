from rest_framework import generics

from .models import Snippet
from .serializers import SnippetSerializer


class SnippetList(generics.ListCreateAPIView):
    """
    Concrete view for listing a queryset or creating a model instance.
    #http://www.cdrf.co/3.9/rest_framework.generics/ListCreateAPIView.html
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance
    #http://www.cdrf.co/3.9/rest_framework.generics/RetrieveUpdateDestroyAPIView.html
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

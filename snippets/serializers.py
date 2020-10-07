from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'owner', 'id', 'title', 'code', 'linenos', 'highlight', 
                'language', 'style']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(view_name='snippet-detail', many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')

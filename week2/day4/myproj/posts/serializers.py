from rest_framework import serializers
from .models import Post
from authapp.serializers import UserSerializer
class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Post
        fields=['id', 'title', 'content','author']
        read_only_fields = ['author']
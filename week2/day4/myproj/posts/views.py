from rest_framework import generics,permissions,filters
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend 

# if he is authenticated => get posts or get one post but he can't create 


class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer     
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self,serializer):
        print("-----------",self.request)
        serializer.save(author=self.request.user)
        
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    
    # filters 
    filter_backends = [filters.SearchFilter]
    search_fields =['title']
    
    
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if self.get_object().author != self.request.user:
            raise PermissionDenied("you don't allowed to update post u not author")
        serializer.save()
        
    def perform_destroy(self, serializer):
        if self.get_object().author != self.request.user:
            raise PermissionDenied("you don't allowed to delete post u not author")
        serializer.save()
        

    
        
        

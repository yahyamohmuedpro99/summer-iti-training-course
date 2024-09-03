from rest_framework import viewsets,generics
from .models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.
# methods 
# v -
# handel for each method 
# v -
# logic get the data then make the processing
# v -
# response 


#  view <=> serilizer <=> model 

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer # serializer 
    queryset = Post.objects.all()  # model - data 
    


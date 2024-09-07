from rest_framework import generics,status
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

# generics 

# signup
class Signup(generics.CreateAPIView):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    
    def create(self,request,*args,**kwargs):
        # create user 
        response=super().create(request,*args,**kwargs) 
        
        # get user
        user=User.objects.get(username=response.data['username'])
        # genereate token
        refresh_token=RefreshToken.for_user(user)
        access_token=refresh_token.access_token
        
        return Response({
            'username': user.username,
            'access_token': str(access_token),
            'refresh_token': str(refresh_token)
            
            },status=status.HTTP_201_CREATED)
        
# /auth/signup/  body:{username,password}
# response => {username,password,token}

# sendr => reciver
# -s = +r

    
    
    
    
    
# login


# list all users on sys 
# => role based 
from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
class Comment(models.Model):
    content=models.TextField()
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.content
    
    
    
    
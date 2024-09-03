from django.db import models


# class author(models.Model):
#     name=models.CharField(max_length=255)
#     email=models.EmailField(max_length=255)
    
    
class Post(models.Model):
    content=models.TextField()
    
    # author=models.ForeignKey()

# class comment(models.Model):
#     content=models.TextField()
#     post=models.ForeignKey(Post)

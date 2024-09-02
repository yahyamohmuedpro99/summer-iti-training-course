from django.db import models

# interaction with database

class Task(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    def __str__(self):
        return self.title 
    


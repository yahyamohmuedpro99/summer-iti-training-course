from django.urls import path
from .views import task_creat


urlpatterns = [
    path('',task_creat,name='task_creat'),
    
]

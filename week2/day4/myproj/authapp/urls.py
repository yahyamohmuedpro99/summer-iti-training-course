from django.urls import path
from .views import Signup


urlpatterns = [
    path('signup/',Signup.as_view(),name='signup')
]

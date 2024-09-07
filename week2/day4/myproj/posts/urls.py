from django.urls import path
from .views import PostCreate,PostList,PostDetail



urlpatterns = [
    path('create/',PostCreate.as_view(),name='create_post'),
    path('',PostList.as_view(),name='list_posts'),
    path('<int:pk>/',PostDetail.as_view(),name='detail_post'),
]

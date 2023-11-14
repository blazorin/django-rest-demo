from django.urls import path

from .views import (
    UserViewSet, TodoViewSet, PostViewSet,
    CommentViewSet, AlbumViewSet, PhotoViewSet, IndexView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
    path('posts/<int:pk>/', PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='post-detail'),

    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    path('comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='comment-detail'),

    path('albums/', AlbumViewSet.as_view({'get': 'list', 'post': 'create'}), name='album-list'),
    path('albums/<int:pk>/', AlbumViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='album-detail'),

    path('photos/', PhotoViewSet.as_view({'get': 'list', 'post': 'create'}), name='photo-list'),
    path('photos/<int:pk>/', PhotoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='photo-detail'),

    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('users/<int:pk>/',UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='user-detail'),

    path('todos/', TodoViewSet.as_view({'get': 'list', 'post': 'create'}), name='todo-list'),
    path('todos/<int:pk>/', TodoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='todo-detail'),

]

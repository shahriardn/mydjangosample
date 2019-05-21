from django.urls import path
from . import views
from .views import PostDetailView, PostCreate, PostUpdateView, PostListView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/create', PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('about/', views.about, name='blog-about')
]

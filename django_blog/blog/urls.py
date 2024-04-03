from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView,
    PostDeleteView, UserPostListView)
from . import views

# for class based views, we use the as_view() function
urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('post/<str:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/', PostCreateView.as_view(), name="post-create"),
    path('post/<str:pk>/update/', PostUpdateView.as_view(),
         name="post-update"),
    path('post/<str:pk>/delete/', PostDeleteView.as_view(),
         name="post-delete"),
    path('user/<str:username>/', UserPostListView.as_view(),
         name="user-posts"),
    path('about/', views.about, name="blog-about"),
]

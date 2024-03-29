from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView
from . import views

# for class based views, we use the as_view() function
urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('post/<str:pk>', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<str:pk>/update', PostUpdateView.as_view(), name="post-update"),
    path('about/', views.about, name="blog-about"),
]

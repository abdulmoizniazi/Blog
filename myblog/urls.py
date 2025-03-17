from django.urls import path
from .views import (PostListView, 
                    PostDetailView, 
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView)
from . import views




app_name = "myblog"
urlpatterns = [
    # path("", views.home, name='home'),
    path("", views.PostListView.as_view(), name='home'),
    path('user/<str:username>', UserPostListView.as_view(), name='users-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path("about/", views.about, name='about'),
]
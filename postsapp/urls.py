from django.urls import path
from . import views
from .views import (PostListView,
PostDetailView,
PostCreateView,
PostUpdateView,
PostDeleteView,
UserPostListView)
urlpatterns = [
    # path('', views.home,name='homepage'),
    path('', PostListView.as_view(),name='homepage'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='postdetails'),
    path('about/', views.about,name='about'),
    path('post/create/', PostCreateView.as_view(),name='postcreate'),
    path('post/<int:pk>/update', PostUpdateView.as_view(),name='postupdate'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(),name='postdelete'),
    path('user/<str:username>', UserPostListView.as_view(),name='userposts'),


]
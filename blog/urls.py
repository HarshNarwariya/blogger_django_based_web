from django.urls import path
from .views import (
    index,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CurrUserPostListView,
    AddCommentView,
    like_view,
    search_post,
)
from . import views

urlpatterns = [
    # path('', PostListView.as_view(), name='blog-home'),
    path('', index, name='blog-home'),
    path('posts/', CurrUserPostListView.as_view(), name='my-posts'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    # path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('tag/<slug:tag_slug>/',views.post_list, name='post_tag'),
    path('search_post/', views.search_post, name='search-post'),
    
    
    path('about/', views.about, name='blog-about'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('like/<int:pk>', like_view, name='like_post'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),
]
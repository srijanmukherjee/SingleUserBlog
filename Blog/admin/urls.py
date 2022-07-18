from django.contrib.auth.decorators import login_required
from django.urls import path, include

from . import views

AUTH_URL = '/admin/auth/'

app_name = 'blog-admin'
urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('', login_required(views.Home.as_view(), login_url=AUTH_URL), name='home'),
    path('posts/', login_required(views.PostListView.as_view(), login_url=AUTH_URL), name='posts'),
    path('post/new', login_required(views.CreatePostView.as_view(), login_url=AUTH_URL), name='create-post'),
    path('post/save', login_required(views.save_post, login_url=AUTH_URL), name='save-post'),
    path('post/edit/<str:slug>', login_required(views.edit_post, login_url=AUTH_URL), name='edit-post'),
    path('post/preview/<str:slug>', login_required(views.preview_post, login_url=AUTH_URL), name='preview-post'),
    path('post/publish/<str:slug>', login_required(views.publish_post, login_url=AUTH_URL), name='publish-post'),
    path('post/archive/<str:slug>', login_required(views.archive_post, login_url=AUTH_URL), name='archive-post'),
    path('post/delete/<str:slug>', login_required(views.delete_post, login_url=AUTH_URL), name='delete-post'),
]

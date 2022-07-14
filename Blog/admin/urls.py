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
    path('post/save', login_required(views.save_post, login_url=AUTH_URL), name='save-post')
]

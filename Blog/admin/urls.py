from django.contrib.auth.decorators import login_required
from django.urls import path, include

from . import views

urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('', login_required(views.Home.as_view(), login_url="auth/"), name='home')
]

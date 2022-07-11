from django.urls import path

from . import views

urlpatterns = [
    path('', views.AuthenticationView.as_view(), name='auth'),
    path('logout/', views.logout_view, name='auth-logout')
]

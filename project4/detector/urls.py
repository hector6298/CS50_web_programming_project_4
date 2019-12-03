from django.urls import path

from . import views


urlpatterns = [
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),
    path('upload/', views.upload_view, name = 'upload'),
    path('home/', views.home_view, name='home'),
]
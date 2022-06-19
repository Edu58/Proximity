from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('home/', views.home, name='home'),
    path('post/', views.post, name='post'),
    path('profile/<username>/', views.profile, name='profile'),
]

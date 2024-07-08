from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('join_meeting/', views.join_meeting_view, name='join_meeting'),
     path('video-conference/', views.new_meeting_view, name='video_conference'),
]

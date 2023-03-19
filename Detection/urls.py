from django.urls import path
from .views import index,webcam_feed



urlpatterns = [
    path('', index, name='index'),
    path('video_feed/', webcam_feed, name='video_feed'),

]

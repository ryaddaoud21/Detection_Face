from django.urls import path
from .views import *



urlpatterns = [
    path('', index, name='index'),
    path('hand/', hand, name='hand'),

    path('video_feed1/', webcam_feed1, name='video_feed1'),
    path('video_feed2/', webcam_feed2, name='video_feed2'),

]

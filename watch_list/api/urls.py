from django.contrib import admin
from django.urls import path
from .views import WatchListAV, WatchDetailAV, StreamingPlatformAV

urlpatterns = [
    # path('list/', movie_list, name='movie_list'), # function based view
    path('list/', WatchListAV.as_view(), name='watch_list'), # class based view
    path('list/<int:pk>', WatchDetailAV.as_view(), name='watch_details'), # class based view
    path('stream/', StreamingPlatformAV.as_view(), name='stream'), # class based view
]

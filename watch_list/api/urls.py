from django.contrib import admin
from django.urls import path
from .views import WatchListAV, ReviewList, ReviewDetail, WatchDetailAV, StreamingPlatformAV,StreamingPlatformDetailAV

urlpatterns = [
    # path('list/', movie_list, name='movie_list'), # function based view
    path('list/', WatchListAV.as_view(), name='watchlist'), # class based view
    path('list/<int:pk>', WatchDetailAV.as_view(), name='watch_detail'), # class based view
    path('stream/', StreamingPlatformAV.as_view(), name='stream'), # class based view
    path('stream/<int:pk>', StreamingPlatformDetailAV.as_view(), name='stream_detail'), # class based view
  
    # path('stream/<int:pk>/review', StreamingPlatformDetailAV.as_view(), name='stream_detail'), # class based view
    path('review/', ReviewList.as_view(), name='review_list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review_details'),
    
]

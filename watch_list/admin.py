from django.contrib import admin

# Register your models here.
from .models import WatchList, StreamingPlatform, Review

admin.site.register(WatchList)
admin.site.register(StreamingPlatform)
admin.site.register(Review)
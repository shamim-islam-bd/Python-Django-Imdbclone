from django.contrib import admin

# Register your models here.
from .models import WatchList, StreamingPlatform

admin.site.register(WatchList)
admin.site.register(StreamingPlatform)
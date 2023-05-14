from django.contrib import admin

# Register your models here.
from watch_list.api.serializers import Movie

admin.site.register(Movie)
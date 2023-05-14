# from django.db import models
from django.db import models

# # Create your models here.

class StreamingPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=100)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name 


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.TextField(max_length=360)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

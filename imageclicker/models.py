from django.db import models

class Gif(models.Model):
    url = models.TextField()
    title = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)


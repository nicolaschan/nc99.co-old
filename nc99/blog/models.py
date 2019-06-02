from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    timestamp = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title + " by " + self.author

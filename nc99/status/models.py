from django.db import models

class Server(models.Model):
    name = models.CharField(max_length=32)
    short_name = models.CharField(max_length=32)
    ip = models.CharField(max_length=32)

    def __str__(self):
        return self.name + "@" + self.ip

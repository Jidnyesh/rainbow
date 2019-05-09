from django.db import models

# Create your models here.
from rainbow.storage_backends import MediaStorage


class Project(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_at = models.DateTimeField(auto_now=True,auto_now_add=False)
    image = models.ImageField()

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=1000)
    location = models.CharField(max_length=2000)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,auto_now=False,null=True)
    date = models.DateField()
    image = models.ImageField()

    def __str__(self):
        return self.title

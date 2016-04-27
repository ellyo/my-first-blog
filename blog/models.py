from django.db import models
from django.utils import timezone

"""
A class uses django models to create the input fields offered when creating a post

"""

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    mood = models.CharField(max_length=20)
    units = models.CharField(max_length=2)
    photo = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):  #Publishes the post when the published date has passed
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

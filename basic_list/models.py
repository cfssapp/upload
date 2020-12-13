from django.db import models
from django.contrib.auth.models import User

class basicList(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')

    def __str__(self):
        return self.title
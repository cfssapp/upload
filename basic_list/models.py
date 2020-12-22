from django.db import models
from django.conf import settings

from django.urls import reverse

class todoList(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner_id', default=1)

    def __str__(self):
        return self.title

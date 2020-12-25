from django.db import models
from django.conf import settings

class todoList(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='todo_post', default=1)

    def __str__(self):
        return self.title

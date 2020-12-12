from django.db import models

# Create your models here.

class basicList(models.Model):
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title
from django.db import models

# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
      
  def __str__(self):
    return self.title

class Article(models.Model):
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title

class basicList(models.Model):
    logo = models.ImageField(default='default.jpg', upload_to='upload_pics')
    title = models.CharField(max_length=100)
    href = models.CharField(max_length=100)
    subDescription = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
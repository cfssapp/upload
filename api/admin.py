from django.contrib import admin
from .models import Task, Article, basicList

# Register your models here.
admin.site.register(Task)
admin.site.register(Article)
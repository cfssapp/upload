from django.db import models
from django.conf import settings

# Create your models here.
class parcelList(models.Model):
    tracking_no = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    parcel_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='parcel_list', default=1)

    def __str__(self):
        return self.title
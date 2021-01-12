import uuid
from django.db import models
from django.conf import settings



# Create your models here.
class Item(models.Model):
    tracking_no = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    item_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='item', default=1)
    ordered = models.BooleanField(default=False)
    cartadded = models.BooleanField(default=False)
    # order_id = models.ForeignKey('Order', on_delete=models.CASCADE, default=29)

    def __str__(self):
        return self.tracking_no


class OrderItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orderitem', default=1)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order', default=1)
    items = models.ManyToManyField(Item)
    shipping_address = models.CharField(max_length=100, default="not set")
    
    def __str__(self):
        return self.user


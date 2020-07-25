# orders/models.py
import uuid
from django.db import models


class Orders(models.Model):
    path = models.CharField(max_length=250)
    orderId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.path
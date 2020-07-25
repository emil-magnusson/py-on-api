from django.db import models
from accesses.models import Accesses


class Option82(models.Model):
    option82 = models.CharField(primary_key=True, unique=True, max_length=250)
    accessId = models.ForeignKey(Accesses, related_name='option82', on_delete=models.PROTECT)

    def __str__(self):
        return self.option82


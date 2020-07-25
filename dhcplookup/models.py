from django.db import models
from accesses.models import Accesses


class Dhcplookup(models.Model):
    ipv4CircuitId = models.CharField(max_length=250, null=True, blank=True)
    ipv4RemoteId = models.CharField(max_length=250, null=True, blank=True)
    ipv6InterfaceId = models.CharField(max_length=250, null=True, blank=True)
    ipv6RemoteId = models.CharField(max_length=250, null=True, blank=True)
    ipv4option82 = models.CharField(max_length=250, null=True, blank=True)
    accessId = models.ForeignKey(Accesses, related_name='dhcplookup', on_delete=models.PROTECT)

    def __str__(self):
        return self.ipv4CircuitId

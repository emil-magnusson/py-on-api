# subscriptions/models.py
import uuid
from django.db import models
from accesses.models import Accesses, Services


class OperationalState(models.Model):
    operationalState = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.operationalState


class Subscriptions(models.Model):
    subscriptionId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    accessId = models.ForeignKey(Accesses, related_name='subscriptions', on_delete=models.PROTECT)
    service = models.ForeignKey(Services, on_delete=models.PROTECT)
    operationalState = models.ForeignKey(OperationalState, on_delete=models.PROTECT)
    spReference = models.CharField(max_length=50, default=uuid.uuid4().hex[:6].upper())
    spSubscriptionId = models.UUIDField(default=uuid.uuid4, editable=False)
    #option82 = models.OneToOneField(Option82, on_delete=models.PROTECT)
    ##dhcpIdentifier
    note = models.CharField(max_length=350, null=True, blank=True)
    ##characteristics

    def __str__(self):
        return '{} - {}'.format(self.service, self.subscriptionId)


class Equipment(models.Model):
    subscriptionId = models.ForeignKey(Subscriptions, related_name='equipment', on_delete=models.PROTECT)
    vendorId = models.CharField(max_length=250)
    macAddress = models.CharField(max_length=250)

    def __str__(self):
        return '{} - {}'.format(self.vendorId, self.macAddress)


# accesses/models.py
import uuid
from django.db import models


class CoNetworkAgreement(models.Model):
    coNetworkAgreement = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.coNetworkAgreement


class PremisesType(models.Model):
    premisesType = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.premisesType


class AccesState(models.Model):
    accessState = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.accessState


class Services(models.Model):
    service = models.CharField(max_length=250)
    connection = models.DateField()
    available = models.DateField()
    disconnection = models.DateField(null=True, blank=True)
    forcedTakeoverPossible = models.BooleanField()

    def __str__(self):
        return self.service


class Accesses(models.Model):
    accessId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    legacyAccessId = models.CharField(max_length=50, default=uuid.uuid4().hex[:6].upper())
    streetName = models.CharField(max_length=250, blank=False)
    streetNumber = models.PositiveSmallIntegerField(null=True, blank=True)
    streetLittera = models.CharField(max_length=250, null=True, blank=True)
    postalCode = models.PositiveSmallIntegerField(blank=False)
    city = models.CharField(max_length=250, blank=False)
    countryCode = models.CharField(max_length=250, blank=False)
    premisesType = models.ForeignKey(PremisesType, on_delete=models.PROTECT)
    mduApartmentNumber = models.PositiveSmallIntegerField(null=True, blank=True)
    mduDistinguisher = models.PositiveSmallIntegerField(null=True, blank=True)
    outlet = models.CharField(max_length=250, null=True, blank=True)
    population = models.CharField(max_length=250, null=True, blank=True)
    accessState = models.ForeignKey(AccesState, on_delete=models.PROTECT)
    coNetworkAgreement = models.ForeignKey(CoNetworkAgreement, on_delete=models.PROTECT)
    services = models.ManyToManyField(Services)
    #subscriptions
    coFiberConverter = models.CharField(max_length=250, null=True, blank=True)
    coCpeSwitch = models.CharField(max_length=250, null=True, blank=True)
    coCpeRouter = models.CharField(max_length=250, null=True, blank=True)


    def __str__(self):
        return '{} {} {}'.format(self.streetName, self.streetNumber, self.streetLittera)



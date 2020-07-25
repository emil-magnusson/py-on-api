from django.db import models


class UnsupportedFields(models.Model):
    unsupportedFields = models.CharField(primary_key=True, max_length=350)

    def __str__(self):
        return self.unsupportedFields


class Endpoints(models.Model):
    name = models.CharField(max_length=250)
    endpoint = models.CharField(max_length=250)
    version = models.CharField(max_length=250)
    documentation = models.CharField(max_length=250)
    note = models.CharField(max_length=350, null=True, blank=True)
    unsupportedFields = models.ManyToManyField(UnsupportedFields, blank=True)

    def __str__(self):
        return self.name
# Create your models here.

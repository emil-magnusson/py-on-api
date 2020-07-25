from django.contrib import admin
from .models import Subscriptions, Equipment, OperationalState

admin.site.register(Subscriptions)
admin.site.register(Equipment)
admin.site.register(OperationalState)


# Register your models here.

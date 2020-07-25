from django.contrib import admin
from .models import Accesses, Services, AccesState, PremisesType, CoNetworkAgreement

admin.site.register(Accesses)
admin.site.register(Services)
admin.site.register(AccesState)
admin.site.register(PremisesType)
admin.site.register(CoNetworkAgreement)
# Register your models here.

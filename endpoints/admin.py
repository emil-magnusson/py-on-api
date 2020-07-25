from django.contrib import admin
from .models import Endpoints, UnsupportedFields

admin.site.register(Endpoints)
admin.site.register(UnsupportedFields)
# Register your models here.

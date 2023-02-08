from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Endpoint)
admin.site.register(models.MLAlgorithm)
admin.site.register(models.MLRequest)
admin.site.register(models.MLAlgorithmStatus)

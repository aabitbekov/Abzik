from django.contrib import admin
from .models import Maintenance, DoneMaintenance, Recomendation, Category

admin.site.register(Category)
admin.site.register(Maintenance)
admin.site.register(DoneMaintenance)
admin.site.register(Recomendation)
from django.contrib import admin
from .models import Vendor, PurchaseOrder, Performance


admin.site.register(Vendor)  # Regitration of vendor
admin.site.register(PurchaseOrder) # Regitration of purchase order
admin.site.register(Performance) # Regitration of performance 

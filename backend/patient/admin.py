from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'mobile_no', 'image']

admin.site.register(Patient, PatientAdmin)

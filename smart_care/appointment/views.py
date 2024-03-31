from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class =  serializers.AppointmentSerializer
    
    def get_queryset(self):
        queryset=super().get_queryset()
        patiend_id=self.request.query_params.get('patiend_id')
        if patiend_id:
            queryset=queryset.filter(patiend_id=patiend_id)
        return queryset
    
            
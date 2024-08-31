from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission


# Create your views here.

class SpecializationViewSet(viewsets.ModelViewSet):
    queryset=models.Specialization.objects.all()
    serializer_class=serializers.SpecializationSerializer
    
    
class DesignationViewSet(viewsets.ModelViewSet):
    queryset=models.Designation.objects.all()
    serializer_class=serializers.DesignationSerializer
    
    
class AvailableTimeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset=models.AvailableTime.objects.all()
    serializer_class=serializers.AvailableTimeSerializer
    
    
class DoctorViewSet(viewsets.ModelViewSet):
    queryset=models.Doctor.objects.all()
    serializer_class=serializers.DoctorSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    
    queryset=models.Review.objects.all()
    serializer_class=serializers.ReviewSerializer
    
    
    
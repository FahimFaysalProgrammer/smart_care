from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.
class AppointmentViewset(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all() # all objects for GET, POST, UPDATE, DELETE.(parent)
    serializer_class = serializers.AppointmentSerializers # object convert to JSON
    
    # custom query kortechi
    def get_queryset(self):
        queryset = super().get_queryset() # 8 no line ke niye aslam or patient(parent) ke inherit korlam
        print(self.request.query_params)
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id = patient_id) # override queryset
        return queryset
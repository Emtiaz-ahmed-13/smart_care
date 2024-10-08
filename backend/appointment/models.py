from django.db import models
from patient.models import Patient
from doctor.models import Doctor, AvailableTime

APPOINTMENT_STATUS = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Running', 'Running'),
]

APPOINTMENT_TYPE = [
    ('Online', 'Online'),
    ('Offline', 'Offline'),
]

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_type = models.CharField(max_length=10, choices=APPOINTMENT_TYPE)
    appointment_status = models.CharField(max_length=10, choices=APPOINTMENT_STATUS, default='Pending')
    symptom = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Patient: {self.patient.user.first_name} - Doctor: {self.doctor.user.first_name}"

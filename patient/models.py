from django.db import models

class Patient_details(models.Model):
    patient_name = models.CharField(max_length = 50)
    contact = models.CharField(max_length = 10)
    admission_date = models.DateField()
    got_discharge = models.BooleanField(default=False)
    ward_number = models.IntegerField()
    total_payment = models.IntegerField()
    disease = models.CharField(max_length = 50)

class Appointments(models.Model):
    patient_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    disease = models.CharField(max_length=50)
    email = models.EmailField()
    date_for_appointment = models.DateField()
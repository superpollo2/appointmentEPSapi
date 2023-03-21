from django.db import models


class Doctor(models.Model):
    doctor_id = models.CharField (max_length= 20, null =False, blank=False, primary_key=True)
    doctor_name = models.CharField (max_length= 100, null=False, blank=False)
    doctor_office = models.IntegerField(default=0, null=False, blank=False)
    
    def __str__(self):
        return self.doctor_id
    
    class Meta:
        verbose_name = 'Doctor'
    
class Patient(models.Model):
    patient_id = models.CharField (max_length=20, null=False, blank=False, primary_key=True)
    patient_name = models.CharField (max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.patient_id
    
    class Meta:
        verbose_name = 'Paciente'
        
class TypeAppointment(models.Model):
    type_id = models.CharField (max_length=10, null=False, blank=False, primary_key=True)
    type_name = models.CharField (max_length=20, null= False, blank=False)
    
    def __str__(self):
        return self.type_name
    
    class Meta:
        verbose_name = 'Tipo de cita medica' 
        
class Appointment(models.Model):
    appointment_id = models.CharField(max_length= 20, null =False, blank=False, primary_key=True)
    date = models.DateField (null=False, blank=False)
    cost = models.FloatField (null=False, blank=False)
    is_done = models.BooleanField (null=False, blank=False, default=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE) 
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_type = models.ForeignKey(TypeAppointment, on_delete=models.CASCADE)
     
    def __str__(self):
        return self.appointment_id
    
    class Meta:
        verbose_name = 'Cita medica'

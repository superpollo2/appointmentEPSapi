from rest_framework import serializers
from ...models import *


class DoctorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Doctor 
        fields = '__all__'
        
    def to_representation(self, instance):
        return {
            
        }
        
class PatientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Patient
        fields = '__all__'
        
    def to_representation(self, instance):
        
        return {
            'patient_id': instance.patient_id,
            'patient_name': instance.patient_name,
        }
        
class TypeAppointmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TypeAppointment
        fields = '__all__'
        
    def to_representation(self, instance):
        
        return {
            'type_id': instance.type_id,
            'type_name': instance.type_name
        }

class AppointmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Appointment
        fields = '__all__'
        
    def to_representation(self, instance):
        
        return {
            'appointment_id': instance.appointment_id,
            'date': instance.date,
            'cost': instance.cost,
            'is_done': instance.is_done,
            'patient': instance.patient.patient_name,
            'doctor': instance.doctor.doctor_name,
            'appointment_tyoe': instance.appointment.type_name
        }
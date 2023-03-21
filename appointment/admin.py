from django.contrib import admin

from django.contrib import admin
from . models import Doctor, Patient, TypeAppointment, Appointment


#models in admin
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(TypeAppointment)

from ..api import GeneralModelViewSet
from ..serializers.serializers import *

class DoctorViewSet(GeneralModelViewSet):
    serializer_class = DoctorSerializer
    
class PatientViewSet(GeneralModelViewSet):
    serializer_class = PatientSerializer
    
class TypeAppointmentViewSet(GeneralModelViewSet):
    serializer_class = TypeAppointmentSerializer

class AppointmentViewSet(GeneralModelViewSet):
    serializer_class = AppointmentSerializer
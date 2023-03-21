from rest_framework.routers import DefaultRouter
from .views.specific_viewset import *

router = DefaultRouter()

router.register(r'doctor', DoctorViewSet, basename='doctor'),
router.register(r'patient', PatientViewSet, basename='patient'),
router.register(r'typeappointement', TypeAppointmentViewSet, basename='typeappointement'),
router.register(r'appointment', AppointmentViewSet, basename = 'appointment')

urlpatterns = router.urls 
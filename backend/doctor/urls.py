from rest_framework.routers import DefaultRouter  
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register('list', views.DoctorViewSet)
router.register('specialization',views.SpecializationViewSet)
router.register('available_time',views.DesignationViewSet)
router.register('degisnation',views.AvailableTimeViewSet)
router.register('reviews',views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

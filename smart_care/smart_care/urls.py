from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static  # Import static
from django.conf import settings  # Import settings module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact_us/', include('contact_us.urls')),
    path('services/',include('service.urls')),
    path('patient/',include('patient.urls')),
    path('doctor/',include('doctor.urls')),
    path('appointment/',include('appointment.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

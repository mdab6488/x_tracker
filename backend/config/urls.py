from django.contrib import admin
from django.urls import path, include
from health.views import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/x/latest/', include('apps.tracker.urls')),
    path('health/', health_check, name='health-check'),
]
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse  # <-- add this import

def health_check(request):
    return JsonResponse({"status": "ok"})  # <-- this is your health check view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('notes.urls')),
    path('healthz/', health_check),  # <-- add this line
]

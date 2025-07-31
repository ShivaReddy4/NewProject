# notes/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
    

       
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
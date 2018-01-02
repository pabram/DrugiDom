from django.urls import path, include
from .views import DocumentViewSet
from .models import Document
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
from django.urls import path, include
from .views import *
from rest_framework import routers
from .models import *

router = routers.DefaultRouter()
router.register(r'documents', DocumentViewSet)
router.register(r'documentTypes', DocumentTypeViewSet)
router.register(r'residents', ResidentViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'roomTypes', RoomTypeViewSet)
router.register(r'staffMembers', StaffMemberViewSet)
router.register(r'dorms', DormViewSet)
router.register(r'users', UserViewSet)
router.register(r'furniture', FurnitureViewSet)
router.register(r'furnitureType', FurnitureTypeViewSet)
router.register(r'electricDevices', ElectricDeviceViewSet)
router.register(r'visits', VisitViewSet)
router.register(r'guests', GuestViewSet)


urlpatterns = [
    path(r'', include(router.urls)),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
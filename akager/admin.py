from django.contrib import admin
from .models import Resident, Guest, StaffMember, Dorm, Visit,\
    Room, RoomType, Furniture, ElectricDevice, FurnitureType, DeviceType


my_models = [
    Resident, Guest, StaffMember, Dorm, Visit, Room,
    RoomType, Furniture, ElectricDevice, FurnitureType, DeviceType
]

admin.site.register(my_models)



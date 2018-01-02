from django.db import models
from django.contrib.auth.models import User


class Resident(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    student_id = models.IntegerField()
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.get_username()


class Guest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()

    def __str__(self):
        return self.user.get_username()


class StaffMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    staff_type = models.IntegerField()
    dorms = models.ForeignKey('Dorm', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.get_username()


class Visit(models.Model):
    guest = models.ForeignKey('Guest', on_delete=models.SET_NULL, null=True)
    resident = models.ForeignKey('Resident', on_delete=models.SET_NULL, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    night_visit = models.BooleanField(default=False)


class Dorm(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    built = models.DateField()
    last_renovation = models.DateField()

    def __str__(self):
        return self.name


class Room(models.Model):
    dorm = models.ForeignKey('Dorm', on_delete=models.CASCADE)
    room_number = models.IntegerField()
    max_beds = models.IntegerField()
    rating = models.DecimalField(decimal_places=5, max_digits=5)
    room_type = models.ForeignKey('RoomType', on_delete=models.SET_NULL, null=True)


class RoomType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Furniture(models.Model):
    production_date = models.DateField()
    condition = models.TextField()
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
    furniture_type = models.ForeignKey('FurnitureType', on_delete=models.SET_NULL, null=True)


class ElectricDevice(models.Model):
    production_date = models.DateField()
    last_service = models.DateField()
    condition = models.TextField()
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
    device_type = models.ForeignKey('DeviceType', on_delete=models.SET_NULL, null=True)


class FurnitureType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class DeviceType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class DocumentType(models.Model):
    name = models.CharField(max_length = 45)
    priority = models.CharField(max_length = 45)
    template = models.CharField(max_length = 45)

    def __str__(self):
        return self.name

class Document(models.Model):
    name = models.CharField(max_length = 45)
    content = models.CharField(max_length = 45)
    case_status = models.CharField(max_length = 45)
    staffMember = models.ForeignKey('StaffMember', on_delete=models.SET_NULL, null=True)
    resident = models.ForeignKey('Resident', on_delete=models.SET_NULL, null=True)
    documentType = models.ForeignKey('DocumentType', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    

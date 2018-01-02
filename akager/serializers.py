from rest_framework import serializers
from .models import *
from django.db import models


class DocumentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DocumentType
        fields = '__all__'


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class ResidentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resident
        fields = '__all__'


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RoomTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'


class StaffMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StaffMember
        fields = '__all__'


class DormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dorm
        fields = '__all__'


class FurnitureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'


class FurnitureTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FurnitureType
        fields = '__all__'


class ElectricDeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ElectricDevice
        fields = '__all__'


class VisitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class GuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        #exclude = ('permission',)
        fields = ('id', 'email', 'first_name',)

# -*- coding: utf8 -*-

from rest_framework import serializers

from .models import Device

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('device_token', 'device_type',)

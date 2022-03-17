


from dataclasses import fields
from .models import SuperType
from rest_framework import serializers


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['types']

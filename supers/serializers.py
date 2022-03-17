from .models import Supers
from rest_framework import serializers


class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ['name','alter_ego','primary_ability','secondary_ability','catchphrase','super_type']
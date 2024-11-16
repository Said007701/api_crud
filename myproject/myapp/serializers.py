from rest_framework import serializers
from .models import Gile

class GileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Gile
        fields = '__all__'
from .models import *
from rest_framework import serializers


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ('id','value')

# создание юзера
    # def create(self, validated_data):

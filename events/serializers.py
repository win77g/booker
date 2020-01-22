from .models import *
from rest_framework import serializers


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id','type','amount','category','date','description',)

# создание юзера
    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)

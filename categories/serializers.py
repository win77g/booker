from .models import *
from rest_framework import serializers


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id','name','capacity')

# создание юзера
    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)

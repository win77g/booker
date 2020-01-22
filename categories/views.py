from django.shortcuts import render
# Create your views here.
from .models import *
from rest_framework import viewsets
from categories.serializers import CategoriesSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class CategoriesIdViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

from django.shortcuts import render

# Create your views here.
from .models import *
from rest_framework import viewsets,permissions,generics
from bill.serializers import BillSerializer


class BillViewSet(viewsets.ModelViewSet):
# class BillViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permissions_classes = [permissions.IsAuthenticated, ]
    queryset = Bill.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BillSerializer

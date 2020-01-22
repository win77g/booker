from django.shortcuts import render

# Create your views here.
from .models import *
from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from events.serializers import EventsSerializer


class EventsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

class EventsIdViewSet(RetrieveAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

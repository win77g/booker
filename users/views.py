from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets,permissions
from users.serializers import UserSerializer




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny, ]
    queryset = User.objects.all().order_by('-date_joined')
    # queryset = User.objects.filter(email = 'win21g@mail.ru')
    serializer_class = UserSerializer
    filter_fields = ('email','username',)

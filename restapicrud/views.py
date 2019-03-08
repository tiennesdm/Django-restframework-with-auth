from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from . import models
from . import serializers


class CrudRestApiList(generics.ListAPIView):
    queryset = models.CrudRestApi.objects.all()
    serializer_class = serializers.CrudRestApiSerializer
class CrudRestApiCreateList(generics.ListCreateAPIView):
    queryset = models.CrudRestApi.objects.all()
    serializer_class = serializers.CrudRestApiSerializer
    permission_classes = (IsAdminUser,)

class CrudRestApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CrudRestApi.objects.all()
    serializer_class = serializers.CrudRestApiSerializer



from rest_framework import serializers
from . import models

class CrudRestApiSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','name', 'title','content')
        model = models.CrudRestApi

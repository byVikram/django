from rest_framework import serializers
from .models import hello

class PeopleSerializers(serializers.ModelSerializer):
    class Meta:
        model = hello
        fields = '__all__' 
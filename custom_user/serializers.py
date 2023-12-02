from rest_framework import serializers
from .models import Owner, Client


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        # write_only=True
    )

    class Meta:
        model = Client
        fields = ['password', 'email']

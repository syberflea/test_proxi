from rest_framework import serializers
from .models import Owner, Client


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    """
    Сериалайзер модели клиента.
    Обеспечивает кодирование пароля перед сохранением в БД.
    """
    password = serializers.CharField(
        # write_only=True
    )

    class Meta:
        model = Client
        fields = ['password', 'email']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save(update_fields=['password'])
        return user

from rest_framework import serializers
from .models import User


# TODO: expecify model fields to be mapped by ModelSerializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "is_superuser",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        raw_password = validated_data.pop("password", None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if raw_password is not None:
            instance.set_password(raw_password)

        instance.save()

        return instance

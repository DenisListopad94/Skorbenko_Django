from django.contrib.auth.models import User
from rest_framework import serializers

from booking_app.models import HotelOwner, Hobby


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, max_length=30)
    first_name = serializers.CharField(required=False, max_length=30)
    last_name = serializers.CharField(required=False, max_length=30)
    email = serializers.EmailField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)

        instance.save()
        return instance


class HotelOwnerSerializer(serializers.Serializer):
    owner_exp_status = serializers.IntegerField()
    first_name = serializers.CharField(required=False, max_length=30)
    last_name = serializers.CharField(required=False, max_length=30)
    email = serializers.EmailField(required=False)

    def create(self, validated_data):
        """
        Создание нового владельца отеля.
        """
        return HotelOwner.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Обновление существующего владельца отеля.
        """
        instance.owner_exp_status = validated_data.get('owner_exp_status', instance.owner_exp_status)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class HobbiesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ["name", "experience"]
import base64
import uuid

from django.core.files.base import ContentFile
from rest_framework import serializers
from .models import User, Coords, Level, Pereval, Image


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'fam', 'name', 'otc', 'phone']


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']


class ImageSerializer(serializers.ModelSerializer):
    # data = serializers.CharField()   #для тестирования api

    class Meta:
        model = Image
        fields = ['data', 'title']
    # сделано для тестирования api
    # def validate_data(self, value):
    #     try:
    #         return ContentFile(base64.b64decode(value), name=f"{uuid.uuid4()}.jpg")
    #     except Exception:
    #         raise serializers.ValidationError("Некорректный формат base64")


class PerevalSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer(required=False)
    images = ImageSerializer(many=True)

    class Meta:
        model = Pereval
        fields = [
            'beauty_title', 'title', 'other_titles', 'connect',
            'add_time', 'user', 'coords', 'level', 'images'
        ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        coords_data = validated_data.pop('coords')
        level_data = validated_data.pop('level', None)
        images_data = validated_data.pop('images')

        # Создание объекта
        user, created = User.objects.get_or_create(
            email=user_data['email'],
            defaults=user_data
        )
        # координаты
        coords = Coords.objects.create(**coords_data)

        # уровень
        level = Level.objects.create(**level_data) if level_data else None

        # перевал
        pereval = Pereval.objects.create(
            user=user,
            coords=coords,
            level=level,
            **validated_data
        )

        # изображения
        for image_data in images_data:
            Image.objects.create(pereval=pereval, **image_data)

        return pereval

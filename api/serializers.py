from rest_framework import serializers
from trader.models import Car, CarPictures, CarManufacturer, CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class CarModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = "__all__"
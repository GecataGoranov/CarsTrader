from django.shortcuts import render, get_object_or_404
from trader.models import Car, CarManufacturer, CarModel, CarPictures
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .serializers import CarSerializer, CarModelsSerializer


class CarsListView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarModelsListView(ListCreateAPIView):
    serializer_class = CarModelsSerializer

    def get_queryset(self):
        manufacturer_id = self.kwargs["manufacturer_id"]
        manufacturer = get_object_or_404(CarManufacturer, id=manufacturer_id)
        return CarModel.objects.filter(manufacturer=manufacturer)
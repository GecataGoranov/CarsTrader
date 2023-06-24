from django.shortcuts import render, get_object_or_404
from trader.models import Car, CarManufacturer, CarModel, CarPictures
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import CarSerializer, CarModelsSerializer, CarFavouriteSerializer


class CarsListView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarModelsListView(ListCreateAPIView):
    serializer_class = CarModelsSerializer

    def get_queryset(self):
        manufacturer_name = self.kwargs["manufacturer_name"]
        manufacturer = get_object_or_404(CarManufacturer, manufacturer=manufacturer_name)
        return CarModel.objects.filter(manufacturer=manufacturer)
    

class CarFavouriteDetailsView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarFavouriteSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        object = Car.objects.get(id=self.kwargs["pk"])
        return object
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.users_who_favourited_car.add(request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
from django.test import TestCase
from trader.models import Car, CarPictures
from accounts.models import TraderUser, TraderProfile

class TestCarDetailsView(TestCase):
    def __create_car(self):
        car_data = {
            'manufacturer': "Peugeot",
            'model': "306 Phase I",
            'category': "SED",
            'gearbox_type': "M",
            'engine_type': "P",
            'engine_power': 88,
            'engine_volume': 1600,
            'eurostandard': 1,
            'mileage': 176000,
            'production_date':"1997-12-12",
            'color': "G",
            'condition': "U",
            'price':2000,
        }
        car = Car.objects.create(**car_data)
        return car

    def test_get_context_data__display_correct_pictures(self):
        car = self.__create_car()
        picture1 = CarPictures.objects.create(picture="media/some_url.jpg", car_id=car)
        picture2 = CarPictures.objects.create(picture="media/some_other_picture.png", car_id=car)
        unmatching_picture = CarPictures.objects.create(picture="media/umnatching_picture.jpg", car_id=3)

    def test_get_context_data__get_correct_seller(self):
        ...

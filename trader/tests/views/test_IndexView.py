from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from trader.models import Car, CarPictures

UserModel = get_user_model()


class TestIndexView(TestCase):
    def test_context_slug_if_authenticated__expect_success(self):
        user_data = {
            "email":"gecata@gosho.store",
            "password":"parola12"
        }

        user = UserModel.objects.create_user(**user_data)

        self.client.login(**user_data)

        response = self.client.get(reverse("index"))

        self.assertEqual(response.context["slug"], "gecatagoshostore")


    def test_context_slug_if_not_authenticated__expect_none(self):
        response = self.client.get("index")

        with self.assertRaises(KeyError):
            slug = response.context["slug"]

    def test_context_car_pictures(self):
        user_data = {
            "email":"gecata@gosho.store",
            "password":"parola12"
        }
        user = UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)

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
        new_car = Car.objects.create(seller=user, **car_data)
        self.assertIsNotNone(new_car)

        new_picture = CarPictures.objects.create(picture="media/car_images/corsa.jpg", car_id=new_car)
        self.assertIsNotNone(new_picture)

        response = self.client.get(reverse("index"))

        self.assertEqual(response.context["car_pictures"], {1: [new_picture]})

        def test_queryset_filter(self):
            ...
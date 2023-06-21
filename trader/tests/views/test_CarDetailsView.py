from django.test import TestCase
from trader.models import Car, CarPictures
from accounts.models import TraderUser, TraderProfile
from django.contrib.auth import login
from django.urls import reverse
from trader.tests.testlib import create_car, create_user_and_profile

class TestCarDetailsView(TestCase):

    def test_get_context_data__display_correct_pictures(self):
        car = create_car()
        car2 = create_car()

        picture1 = CarPictures.objects.create(picture="media/some_url.jpg", car_id=car)
        picture2 = CarPictures.objects.create(picture="media/some_other_picture.png", car_id=car)
        unmatching_picture = CarPictures.objects.create(picture="media/umnatching_picture.jpg", car_id=car2)

        response = self.client.get(reverse("details", args=[car.id]))

        self.assertEqual(response.context["pictures"].count(), 2)

    def test_get_context_data__get_correct_seller(self):
        _, profile = create_user_and_profile()
        car = create_car()

        response = self.client.get(reverse("details", args=[car.id]))

        self.assertEqual(response.context["car_seller"], profile)

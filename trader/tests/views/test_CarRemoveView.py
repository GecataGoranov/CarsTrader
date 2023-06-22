from django.test import TestCase
from trader.models import Car, CarPictures
from accounts.models import TraderUser, TraderProfile
from django.urls import reverse
from django.contrib.auth import login
from trader.tests.testlib import TestLibMixin


class TestCarRemoveView(TestLibMixin, TestCase):

    def test_get__car_to_delete__expect_to_show_template(self):
        car = self.create_car()
        car_id = car.id

        response = self.client.get(reverse("delete car", args=[car_id]))

        self.assertEqual(car_id, car.id)

    def test_get__success_if_seller__and_show_correct_template(self):
        user, _ = self.create_user_and_profile()
        car = self.create_car()

        self.client.login(user=user)
        
        response = self.client.get(reverse("delete car", args=[car.id]))

        self.assertTemplateUsed("trader/confirm_delete.html")

    def test_get__redirect_if_not_seller(self):
        user, _ = self.create_user_and_profile()
        car = self.create_car()
        another_user = self.create_another_user()

        self.client.login(user=another_user)

        response = self.client.get(reverse("delete car", args=[car.id]))
        self.assertRedirects(response, expected_url=reverse("prohibited"))

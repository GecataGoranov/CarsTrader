from django.test import TestCase
from trader.tests.testlib import TestLibMixin
from django.urls import reverse
from trader.models import Car
from accounts.models import TraderUser
from django.contrib.auth import authenticate


class TestFavouriteView(TestLibMixin, TestCase):
    def test_if_user_is_authenticated__expect_correct_car_favourited(self):
        user, _ = self.create_user_and_profile_and_login()
        another_user = self.create_another_user()
        
        car1 = self.create_car()
        car2 = self.create_car(model="Peugeot 306 Phase II")

        response = self.client.get(reverse("favourite", kwargs={"pk": car1.id}))

        print(car1.users_who_favourited_car.all())

        self.assertRedirects(response, reverse("index"))
        

    def test_if_user_is_not_authenticated__expect_redirect_to_login(self):
        ...
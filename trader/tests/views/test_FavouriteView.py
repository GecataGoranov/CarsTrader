from django.test import TestCase
from trader.tests.testlib import create_user_and_profile, create_another_user, create_car
from django.urls import reverse
from trader.models import Car
from accounts.models import TraderUser


class TestFavouriteView(TestCase):
    def test_if_user_is_authenticated__expect_correct_car_favourited(self):
        user, _ = create_user_and_profile()
        another_user = create_another_user()
        self.client.login(user=user)
        
        car1 = create_car()
        car2 = create_car(model="Peugeot 306 Phase II")

        response = self.client.get(reverse("favourite", kwargs={"pk": car1.id}))
        car = Car.objects.get(id=car1.id)
        print(car.users_who_favourited_car.all())

        self.assertRedirects(response, reverse("index"))

    def test_if_user_is_not_authenticated__expect_redirect_to_login(self):
        ...
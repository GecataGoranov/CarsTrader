from accounts.models import TraderUser, TraderProfile
from trader.models import Car, CarPictures
from django.contrib.auth import get_user_model, login
from django.test import TestCase


UserModel = get_user_model()


class TestLibMixin(TestCase):
    valid_user_credentials = {
            "email":"test@gosho.store",
            "password":"test1234"}
    def create_user_and_profile(self):
        user = UserModel.objects.create(**self.valid_user_credentials)
        valid_profile_credentials = {
            "user":user,
            "slug":"testgoshostore",
            "profile_picture":"some_picture.png",
            "phone_number":"0909090909",
            "first_name":"Test",
            "last_name":"User",
            "place_of_living":"TestLand"
        }

        profile = TraderProfile.objects.create(**valid_profile_credentials)
        return user, profile

    def create_car(self, model="306 Phase I"):
        car_data = {
            'manufacturer': "Peugeot",
            'model': model,
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

        try:
            user = UserModel.objects.get(email="test@gosho.store")
        except:
            user ,_ = self.create_user_and_profile()

        car = Car.objects.create(seller=user, **car_data)
        return car

    def create_another_user(self, **credentials):
        if not credentials:
            credentials = {
                "email":"another_test@gosho.store",
                "password":"test1234"}
        user = UserModel.objects.create(**credentials)
        return user

    def create_user_and_profile_and_login(self):
        user, profile = self.create_user_and_profile()
        self.client.login(**self.valid_user_credentials)
        return user, profile
        
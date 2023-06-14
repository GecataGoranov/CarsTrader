from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from trader.models import Car
from accounts.models import TraderProfile


UserModel = get_user_model()

class TestPublishCreateView(TestCase):
    def test_context_slug_if_authenticated__expect_success(self):
        self.user_login()

        response = self.client.get(reverse("index"))

        self.assertEqual(response.context["slug"], "gecatagoshostore")


    def test_context_slug_if_not_authenticated__expect_none(self):
        response = self.client.get("index")

        with self.assertRaises(KeyError):
            slug = response.context["slug"]

    def test_form_valid_saving_seller_with_authenticated_user__expect_success(self):
        self.user_login()
        TraderProfile.objects.create(user=self.user, first_name="Gosho")


        form_data = {
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
            'region':"Smolyan",
            'place':"Smolyan",
            'picture':"media/car_pictures/peugeot.jpg"
        }

        response = self.client.post(reverse("publish"), data=form_data)
        self.assertEqual(response.status_code, 200)


    def test_form_valid_saving_seller_without_authenticated_user__expect_fail(self):
        ...

    def test_get_redirection_if_no_first_name__expect_redirect(self):
        self.user_login()
        TraderProfile.objects.create(user=self.user)

        response = self.client.get(reverse("publish"))

        self.assertRedirects(response, expected_url=reverse("add info", kwargs={"slug":"gecatagoshostore"}))

    def test_stay_on_page_if_first_name__expect_form_template(self):
        self.user_login()
        TraderProfile.objects.create(user=self.user, first_name="Gosho")


        response = self.client.get(reverse("publish"))

        self.assertTemplateUsed(response, "trader/publish.html")
        

    def user_login(self):
        user_data = {
                "email":"gecata@gosho.store",
                "password":"parola12"
            }

        self.user = UserModel.objects.create_user(**user_data)

        self.client.login(**user_data)

from django.urls import path
from .views import CarsListView, CarModelsListView


urlpatterns = [
    path("cars", CarsListView.as_view(), name="cars api"),
    path("models/<int:manufacturer_id>", CarModelsListView.as_view(), name="models api")
]
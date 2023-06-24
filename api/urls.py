from django.urls import path
from .views import CarsListView, CarModelsListView, CarFavouriteDetailsView


urlpatterns = [
    path("cars", CarsListView.as_view(), name="cars api"),
    path("models/<str:manufacturer_name>", CarModelsListView.as_view(), name="models api"),
    path("favourite/<int:pk>", CarFavouriteDetailsView.as_view(), name="favourite api")
]
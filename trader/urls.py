from django.urls import path
from .views import IndexView, PublishCreateView, CarDetailsView



urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("publish", PublishCreateView.as_view(), name="publish"),
    path("details/<int:pk>", CarDetailsView.as_view(), name="details")
]
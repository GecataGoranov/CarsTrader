from django.urls import path
from .views import IndexView, PublishCreateView, CarDetailsView, CarRemoveView, FavouriteView
from django.views.generic import TemplateView



urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("publish", PublishCreateView.as_view(), name="publish"),
    path("details/<int:pk>", CarDetailsView.as_view(), name="details"),
    path("delete/<int:pk>", CarRemoveView.as_view(), name="delete car"),
    path("prohibited", TemplateView.as_view(template_name="base/prohibited"), name="prohibited"),
    path("favourite/<int:pk>", FavouriteView.as_view(), name="favourite")
]
from django.urls import path
from .views import IndexView, RegisterView, CustomLoginView, CustomLogoutView, PublishCreateView, CarDetailsView, login_view



urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("register", RegisterView.as_view(), name="register"),
    path("login", login_view, name="login"),
    path("logout", CustomLogoutView.as_view(), name="logout"),
    path("publish", PublishCreateView.as_view(), name="publish"),
    path("details/<int:pk>", CarDetailsView.as_view(), name="details")
]
from django.urls import path
from .views import RegisterView, UserLoginView, UserLogoutView, ProfilePageView, AddInfoView


urlpatterns = (
    path("register", RegisterView.as_view(), name="register"),
    path("login", UserLoginView.as_view(), name="login"),
    path("logout", UserLogoutView.as_view(), name="logout"),
    path("profile/<slug:slug>", ProfilePageView.as_view(), name="profile"),
    path("add_info/<slug:slug>", AddInfoView.as_view(), name="add info")
)
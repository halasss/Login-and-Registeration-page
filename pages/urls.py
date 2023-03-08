from django.urls import path
from .views import LoginPageView, RegisterPageView


urlpatterns = [
path("", LoginPageView.as_view(), name="home"),
path("register", RegisterPageView.as_view(), name="register"),
]

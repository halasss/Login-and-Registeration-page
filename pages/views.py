from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class LoginPageView(TemplateView):
    template_name = "login.html"


class RegisterPageView(TemplateView):
    template_name = "register.html"

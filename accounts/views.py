from typing import Any
from django.db import models
from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.utils.text import slugify

from .forms import CreateTraderUserForm
from .models import TraderProfile, TraderUser

# Create your views here.
class RegisterView(CreateView):
    template_name = "accounts/register.html"
    form_class = CreateTraderUserForm
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "register"
        return context
    
    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        new_profile = TraderProfile.objects.create(user_id=self.object, slug=slugify(self.object.email))
        return result
    

class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    success_url = reverse_lazy("index")

    def get_success_url(self):
        return self.success_url
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "login"
        return context

    
class UserLogoutView(LogoutView):
    next_page = reverse_lazy("index")


class ProfilePageView(DetailView):
    template_name = "accounts/profile.html"
    model = TraderProfile
    context_object_name = "user"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.prefetch_related("user_id")
        return queryset
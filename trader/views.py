from typing import Any, Dict
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .forms import FilterForm, PublishForm
from .models import Car, CarPictures



# Create your views here.

class IndexView(FormView, ListView):
    template_name = "trader/index.html"
    form_class = FilterForm
    success_url = reverse_lazy("index")
    model = Car
    context_object_name = "cars"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "home"
        return context
    

class RegisterView(CreateView):
    template_name = "trader/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "register"
        return context
    

class CustomLoginView(LoginView):
    template_name = "trader/login.html"
    success_url = reverse_lazy("index")

    def get_success_url(self):
        return self.success_url
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "login"
        return context
    
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("index")


@method_decorator(login_required(login_url="/login"), name="dispatch")
class PublishCreateView(CreateView):
    template_name = "trader/publish.html"
    form_class = PublishForm
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "publish"
        return context
    
    def form_valid(self, form):
        form.instance.seller = self.request.user
        car = form.save(commit=False)
        car.save()

        pictures = self.request.FILES.getlist("pictures")
        for picture in pictures:
            CarPictures.objects.create(car_id=car, picture=picture)

        return super().form_valid(form)

    

class CarDetailsView(DetailView):
    template_name = "trader/car_details.html"
    model = Car
    context_object_name = "car"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pictures = CarPictures.objects.filter(car_id=self.object)
        context["pictures"] = pictures
        return context
        
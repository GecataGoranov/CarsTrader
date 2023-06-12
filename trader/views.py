from typing import Any, Dict
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.utils.text import slugify

from .forms import FilterForm, PublishForm
from .models import Car, CarPictures
from accounts.models import TraderUser, TraderProfile




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
        
        if self.request.user.is_authenticated:
            context["slug"] = slugify(self.request.user.email)

        car_pictures = CarPictures.objects.select_related("car_id")
        car_pictures_dict = {}
        for car_picture in car_pictures:
            car_pictures_dict.setdefault(car_picture.car_id_id, []).append(car_picture)
        context["car_pictures"] = car_pictures_dict

        return context
    
    def get_queryset(self):
        filters = {
            'manufacturer__contains': self.request.GET.get("manufacturer", ""),
            'model__contains': self.request.GET.get("model", ""),
            'category__contains': self.request.GET.get("category", ""),
            'gearbox_type__contains': self.request.GET.get("gearbox_type", ""),
            'engine_type__contains': self.request.GET.get("engine_type", ""),
            'engine_power__gte': int(self.request.GET.get("engine_power", 0) or 0),
            'engine_volume__gte': int(self.request.GET.get("engine_volume", 0) or 0),
            'eurostandard__gte': int(self.request.GET.get("eurostandard", 0) or 0),
            'mileage__lte': int(self.request.GET.get("mileage", 20000000) or 20000000),
            'color__contains': self.request.GET.get("color", ""),
            'condition__icontains': self.request.GET.get("condition", ""),
        }

        filters = {key: value for key, value in filters.items() if value != ""}

        return Car.objects.filter(**filters)


class PublishCreateView(LoginRequiredMixin, CreateView):
    template_name = "trader/publish.html"
    form_class = PublishForm
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "publish"
        if self.request.user.is_authenticated:
            context["slug"] = slugify(self.request.user.email)
        return context
    
    def form_valid(self, form):
        form.instance.seller = self.request.user
        car = form.save(commit=False)
        car.save()

        pictures = self.request.FILES.getlist("pictures")
        for picture in pictures:
            CarPictures.objects.create(car_id=car, picture=picture)

        return super().form_valid(form)
    
    def get(self, request, *args, **kwargs):
        user_profile = TraderProfile.objects.get(user=self.request.user)
        if not user_profile.first_name:
            return redirect("add info", slug=user_profile.slug)
        return super().get(request, *args, **kwargs)


class CarDetailsView(DetailView):
    template_name = "trader/car_details.html"
    model = Car
    context_object_name = "car"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.get_object()
        pictures = CarPictures.objects.filter(car_id=self.object)
        car_seller = TraderProfile.objects.prefetch_related("user").get(user=car.seller)
        context["car_seller"] = car_seller
        context["pictures"] = pictures
        if self.request.user.is_authenticated:
            context["slug"] = slugify(self.request.user.email)
        return context
    
    


from typing import Any, Dict
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
        return context
    

@method_decorator(login_required(login_url="accounts/login"), name="dispatch")
class PublishCreateView(CreateView):
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


class CarDetailsView(DetailView):
    template_name = "trader/car_details.html"
    model = Car
    context_object_name = "car"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pictures = CarPictures.objects.filter(car_id=self.object)
        context["pictures"] = pictures
        if self.request.user.is_authenticated:
            context["slug"] = slugify(self.request.user.email)
        return context
    


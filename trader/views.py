from typing import Any, Dict
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .forms import FilterForm, PublishForm, CreateTraderUserForm
from .models import Car, CarPictures
from django.contrib.auth import login, authenticate



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
    form_class = CreateTraderUserForm
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "register"
        return context
    
    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result
    

class CustomLoginView(LoginView):
    template_name = "trader/login.html"
    success_url = reverse_lazy("index")

    def get_success_url(self):
        return self.success_url
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "login"
        return context

    
    def form_invalid(self, form):
        return HttpResponse()
        pass


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
        else:
            return HttpResponse("UZUNOV")
    else:
        form = AuthenticationForm
        return render(request, "trader/login.html", {"page":"login",
                                                     "form":form})
    
    
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

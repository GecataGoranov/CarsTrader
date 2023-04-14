from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy



# Create your views here.

class IndexView(TemplateView):
    template_name = "trader/index.html"

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
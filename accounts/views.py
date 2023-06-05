from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms import CreateTraderUserForm


# Create your views here.
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
    

class UserLoginView(LoginView):
    template_name = "trader/login.html"
    success_url = reverse_lazy("index")

    def get_success_url(self):
        return self.success_url
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "login"
        return context

    
class UserLogoutView(LogoutView):
    next_page = reverse_lazy("index")
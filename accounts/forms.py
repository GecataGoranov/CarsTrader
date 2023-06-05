from django.contrib.auth.forms import BaseUserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import TraderProfile


UserModel = get_user_model()

class CreateTraderUserForm(BaseUserCreationForm):

    class Meta:
        model = UserModel
        fields = ("email",)

    def save(self, commit=True):
        return super().save(commit=commit)
    

class AddInfoForm(forms.ModelForm):

    class Meta:
        model = TraderProfile
        fields = "__all__"
        exclude = ("user_id", "slug")
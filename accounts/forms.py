from django.contrib.auth.forms import BaseUserCreationForm
from django.contrib.auth import get_user_model


UserModel = get_user_model()

class CreateTraderUserForm(BaseUserCreationForm):

    class Meta:
        model = UserModel
        fields = ("email",)

    def save(self, commit=True):
        return super().save(commit=commit)
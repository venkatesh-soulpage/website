from django import forms
from .models import Treasure
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TreasureForm(forms.ModelForm):
    class Meta:
        model = Treasure
        fields = ["name", "value", "material", "location", "image"]


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Optional.")
    last_name = forms.CharField(max_length=30, required=False, help_text="Optional.")
    email = forms.EmailField(
        max_length=254, help_text="Required. Inform a valid email address."
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "email",
        )


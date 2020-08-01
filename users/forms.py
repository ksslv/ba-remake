from django import forms
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from . import models


class RegistrationForm(forms.ModelForm):
    """ 
    A form to register new users. 
    """

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "PASSWORD"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "CONFIRM PASSWORD"})
    )

    class Meta:
        model = models.User
        fields = ("username", "email")

        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "USERNAME"}),
            "email": forms.EmailInput(attrs={"placeholder": "EMAIL ADDRESS"}),
        }

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            models.User.objects.get(username=username)
            raise forms.ValidationError("Username is not available")
        except models.User.DoesNotExist:
            return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("Email is not available")
        except models.User.DoesNotExist:
            return email

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if not password2:
            raise forms.ValidationError("Please re-type your password")
        if password != password2:
            raise forms.ValidationError("Passwords do not match")
        return password


class LoginForm(forms.Form):
    """ 
    A form to authenticate users against the database. 
    """

    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "USERNAME"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "PASSWORD"})
    )

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        try:
            user = models.User.objects.get(username=username)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error(
                    "password", forms.ValidationError("Password is incorrect")
                )
        except models.User.DoesNotExist:
            self.add_error("username", forms.ValidationError("User does not exist"))


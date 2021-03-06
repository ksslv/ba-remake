from django import forms
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from . import models


class EditProfileForm(forms.ModelForm):
    """
    A form for users to update their profile information.
    """

    class Meta:
        model = models.User
        fields = (
            "first_name",
            "last_name",
            "username",
            "bio",
            # "chef_level",
            "profile_photo",
        )

        widgets = {
            "first_name": forms.TextInput(
                attrs={"style": "width:370px", "class": "px-1"}
            ),
            "last_name": forms.TextInput(
                attrs={"style": "width:370px", "class": "px-1"}
            ),
            "username": forms.TextInput(
                attrs={"style": "width:370px", "class": "px-1"}
            ),
            "bio": forms.Textarea(attrs={"style": "width:370px", "class": "px-1"}),
            # "chef_level": forms.Select(attrs={"style": "width:360px", "class": "px-1"}),
            "profile_photo": forms.FileInput,
        }

        labels = {
            "profile_photo": "Change Profile Photo",
        }


class RegistrationForm(forms.ModelForm):
    """ 
    A form to register new users. 
    """

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"style": "width:370px", "class": "px-1"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"style": "width:370px", "class": "px-1"}),
        label="Confirm Password",
    )

    class Meta:
        model = models.User
        fields = ("username", "email")

        widgets = {
            "username": forms.TextInput(
                attrs={"style": "width:370px", "class": "px-1"}
            ),
            "email": forms.EmailInput(attrs={"style": "width:370px", "class": "px-1"}),
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
        widget=forms.TextInput(attrs={"style": "width:370px", "class": "px-1"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"style": "width:370px", "class": "px-1"})
    )

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        try:
            user = models.User.objects.get(username=username)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", "Password is incorrect")
        except models.User.DoesNotExist:
            self.add_error("username", forms.ValidationError("User does not exist"))

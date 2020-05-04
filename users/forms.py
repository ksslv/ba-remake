from django import forms
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    # TODO:
    #   handle cases where user does not exist or password is incorrect

from django.shortcuts import render
from django.views import View
from . import forms


# Create your views here.
class LoginView(View):
    """
    Provides the ability to login as a user with a username/email and password.
    
    """

    def get(self, request):
        pass

    def post(self, request):
        pass

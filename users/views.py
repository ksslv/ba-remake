from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import DetailView, UpdateView
from . import forms, models


class UserProfileView(DetailView):
    """
    A view to display user profile.
    """

    model = models.User
    context_object_name = "user_profile"


class UserProfileEditView(UpdateView):
    """
    A view that displays a form for editing a user profile,
    displays any validation errors, and saves changes to the User object.
    """

    model = models.User
    template_name = "users/edit_profile.html"
    form_class = forms.EditProfileForm

    def get_object(self, queryset=None):
        return self.request.user


def register(request):
    """
    A method that saves a new user to the database and logs them in with redirecting to the main page.
    """
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password")
            user.set_password(password)
            user.save()

            login(request, user)

            return redirect("core:home")

    else:
        form = forms.RegistrationForm()
    return render(
        request=request, template_name="users/register.html", context={"form": form}
    )


def log_in(request):
    """
    A method that authenticates the user and creates a new user session.
    """
    if request.method == "POST":
        form = forms.LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("core:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    form = forms.LoginForm()
    return render(
        request=request, template_name="users/login.html", context={"form": form}
    )


def log_out(request):
    """
    A method to log out a user. Returns a redirect to home page. 
    """
    logout(request)
    return redirect("core:home")

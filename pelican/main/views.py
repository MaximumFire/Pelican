from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UpdateUserForm, UpdateProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

def index(response):
    return render(response, "main/index.html", {})

def home(response):
    return render(response, "main/home.html", {})

def download(response):
    return render(response, "main/download.html", {})

def support(response):
    return render(response, "main/support.html", {})

def about(response):
    return render(response, "main/about.html", {})

def tos(response):
    return render(response, "main/tos.html", {})

@login_required
def profile(response):
    if response.method == 'POST':
        user_form = UpdateUserForm(response.POST, instance=response.user)
        profile_form = UpdateProfileForm(response.POST, response.FILES, instance=response.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(response, 'Your profile is updated successfully')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=response.user)
        profile_form = UpdateProfileForm(instance=response.user.profile)

    return render(response, 'main/profile.html', {'user_form': user_form, 'profile_form': profile_form})

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'main/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')


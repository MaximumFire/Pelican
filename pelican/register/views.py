from tkinter.tix import Tree
from urllib import request
from django.shortcuts import redirect, render
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.

def register(response):
    if response.method == "POST":
        form = CreateUserForm(response.POST)
        if form.is_valid():
            username, email, password = form.cleaned_data["username"], form.cleaned_data['email'], form.cleaned_data['password1']
            new_user = User.objects.create_user(username, email, password)
            new_user.is_active = True
            new_user.save()
            return redirect("/home")
    else:  
        form = CreateUserForm()

    return render(response, "register/register.html", {"form": form})

def logout_page(response):
    if str(response.user) == "AnonymousUser":
        logged_in = False
    else:
        logged_in = True
    logout(response)
    return render(response, "registration/logout.html", {"logged_in": logged_in})
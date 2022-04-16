from django.shortcuts import redirect, render
from .forms import CreateUserForm
from django.contrib.auth.models import User

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
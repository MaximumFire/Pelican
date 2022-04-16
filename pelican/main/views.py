from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return render(response, "main/index.html", {})

def login(response):
    return render(response, "main/login.html", {})

def register(response):
    return render(response, "main/register.html", {})

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

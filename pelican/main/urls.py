from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("download/", views.download, name="download"),
    path("support/", views.support, name="support"),
    path("about/", views.about, name="about"),
    path("tos/", views.tos, name="tos"),
    path("profile/", views.profile, name="profile"),
    path('password-change/', views.ChangePasswordView.as_view(), name='password-change'),
]
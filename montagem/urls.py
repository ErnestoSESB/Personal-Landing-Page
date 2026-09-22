from django.urls import path

from . import views

app_name = "montagem"

urlpatterns = [
    path("", views.home, name="home"),
    path("", views.home, name="home"),
]

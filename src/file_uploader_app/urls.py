from django.urls import path
from file_uploader_app import views

urlpatterns = [
    path("", views.home, name="home"),
]
from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("thanks/", views.thanks, name="thanks")
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("finchs/", views.all_finches, name="about"),
    path("finchs/<int:finch_id>", views.finch_details, name="details"),
]

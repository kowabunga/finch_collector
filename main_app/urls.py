from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("finchs/", views.all_finches, name="about"),
    path("finchs/<int:finch_id>", views.finch_details, name="details"),
    path("finchs/create/", views.CreateFinch.as_view(), name="finchs_create"),
    path("finchs/<int:pk>/update/", views.UpdateFinch.as_view(), name="finchs_update"),
    path("finchs/<int:pk>/delete/", views.DeleteFinch.as_view(), name="finchs_delete"),
]

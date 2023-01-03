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
    path("finchs/<int:finch_id>/add_foodtype/", views.add_foodtype, name="add_foodtype"),
    path("finchs/<int:finch_id>/assoc_toy/<int:toy_id>/", views.assoc_toy, name="assoc_toy"),
    path("toys/", views.ToyList.as_view(), name="toys_index"),
    path("toys/<int:pk>/", views.ToyDetail.as_view(), name="toys_details"),
    path("toys/create/", views.ToyCreate.as_view(), name="toys_create"),
    path("toys/<int:pk>/update/", views.ToyUpdate.as_view(), name="toys_update"),
    path("toys/<int:pk>/delete/", views.ToyDelete.as_view(), name="toys_delete"),
]

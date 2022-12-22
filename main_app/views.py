from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Finch


class CreateFinch(CreateView):
    model = Finch
    fields = "__all__"


class UpdateFinch(UpdateView):
    model = Finch
    fields = ["color", "description", "age"]


class DeleteFinch(DeleteView):
    model = Finch
    success_url = "/finchs/"


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def all_finches(request):
    finchs = Finch.objects.all()
    return render(request, "finchs/index.html", {"finchs": finchs})


def finch_details(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, "finchs/details.html", {"finch": finch})

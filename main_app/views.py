from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FoodTypeForm

from .models import Finch, Toy


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

    food_form = FoodTypeForm()

    toys_finch_does_not_have = Toy.objects.exclude(id__in=finch.toys.all().values_list("id"))

    return render(
        request,
        "finchs/details.html",
        {
            "finch": finch,
            "food_form": food_form,
            "toys": toys_finch_does_not_have,
        },
    )


def add_foodtype(request, finch_id):
    form = FoodTypeForm(request.POST)

    if form.is_valid():
        new_food = form.save(commit=False)

        new_food.finch_id = finch_id
        new_food.save()

    return redirect("details", finch_id=finch_id)


def assoc_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    return redirect("details", finch_id=finch_id)


class ToyList(ListView):
    model = Toy


class ToyDetail(DetailView):
    model = Toy


class ToyCreate(CreateView):
    model = Toy
    fields = "__all__"


class ToyUpdate(UpdateView):
    model = Toy
    fields = ["name", "funness_scale"]


class ToyDelete(DeleteView):
    model = Toy
    success_url = "/toys/"

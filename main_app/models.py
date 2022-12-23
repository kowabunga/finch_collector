from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(200)
    age = models.IntegerField()

    def get_absolute_url(self):
        # first arg is name of a url
        # looks at kwargs in urls.py
        return reverse("details", kwargs={"finch_id": self.id})


FOOD_TYPES = (
    ("S", "Seeds"),
    ("G", "Grains"),
    ("F", "Fruits"),
    ("B", "Berries"),
)

AMOUNTS = (
    ("S", "Small"),
    ("M", "Medium"),
    ("L", "Large"),
)


class FoodType(models.Model):
    type = models.CharField(
        max_length=1,
        choices=FOOD_TYPES,
        default=FOOD_TYPES[0][0],
    )

    amounts = models.CharField(
        max_length=1,
        choices=AMOUNTS,
        default=AMOUNTS[0][0],
    )

    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"Needs {self.get_food_display()} in a {self.get_food_display()} quantity."

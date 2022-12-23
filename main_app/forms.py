from django.forms import ModelForm
from .models import FoodType


class FoodTypeForm(ModelForm):
    class Meta:
        model = FoodType
        fields = ["type", "amounts"]

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

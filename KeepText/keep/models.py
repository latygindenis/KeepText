from django.db import models
from django.utils import timezone

class Zametka(models.Model):
    header = models.CharField(max_length=200, default="")
    text = models.CharField(max_length=5000, default="")
    time_field = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.header


# Create your models here.

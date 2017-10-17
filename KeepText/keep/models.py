from django.db import models


class Zametka(models.Model):
    header = models.CharField(max_length=200)
    text = models.CharField(max_length=5000)
    time_field = models.DateTimeField(default=None)

    def __str__(self):
        return self.header

# Create your models here.

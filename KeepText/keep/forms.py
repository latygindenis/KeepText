from django import forms
from .models import *

class ZametkaForm(forms.ModelForm):

    class Meta:
        model = Zametka
        exclude = ["time_field"]
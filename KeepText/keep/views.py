from django.shortcuts import render, get_object_or_404
from keep.models import Zametka
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    zametka = Zametka.objects.order_by('time_field')[:5]
    context = {'zametka':zametka}
    return render(request, 'keep/index.html', context)

# Create your views here.

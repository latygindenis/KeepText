from django.shortcuts import render, get_object_or_404
from keep.models import Zametka
from django.http import HttpResponseRedirect, HttpResponse
from .forms import ZametkaForm

def index(request):
    zametka = Zametka.objects.order_by('-time_field')[:5]
    context = {'zametka':zametka}
    form = ZametkaForm(request.POST or None)
    if request.method == "POST":
        new_form = form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'keep/index.html', locals())

# Create your views here.

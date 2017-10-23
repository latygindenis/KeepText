from django.shortcuts import render, get_object_or_404,redirect
from keep.models import Zametka
from django.http import HttpResponseRedirect, HttpResponse
from .forms import ZametkaForm



def index(request):
    zametka = Zametka.objects.order_by('-time_field')[:10]
    context = {'zametka':zametka}
    form = ZametkaForm(request.POST or None)
    if request.method == "POST":
        new_form = form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'keep/index.html', locals())

def del_keep(request, a_id):
    mydelkeep = Zametka.objects.get(id=a_id)
    print(1)
    mydelkeep.delete()
    return redirect('/keep')

# Create your views here.

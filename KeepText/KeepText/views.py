from django.shortcuts import render, get_object_or_404,redirect

def my_homepage_view(request):
    return render(request, 'KeepText/start.html')

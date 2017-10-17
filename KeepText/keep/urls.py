from django.conf.urls import *
from keep import views

urlpatterns = [url(r'^$', views.index, name='index'),
                    ]
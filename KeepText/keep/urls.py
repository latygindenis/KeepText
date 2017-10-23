from django.conf.urls import *
from keep import views

urlpatterns = [url(r'^$', views.index, name='index'),
                    url(r'^(\d+)/del/$', views.del_keep, name='del_keep'),]
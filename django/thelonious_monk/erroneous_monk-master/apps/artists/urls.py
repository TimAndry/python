from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<id>\d+)$', views.show),
    url(r'^(?P<id>\d+)/edit$', views.edit),
    url(r'^(?P<id>\d+)/update$', views.update),
    url(r'^(?P<id>\d+)/delete$', views.delete),
    url(r'^(?P<id>\d+)/create_album$', views.create_album),
    url(r'^', views.index),
]
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^update$', views.update),
    url(r'^clear$', views.clear)
]
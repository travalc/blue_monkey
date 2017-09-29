from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^add_trip', views.add_trip, name='add_trip'),
    url(r'^join', views.join, name='join'),
    url(r'^destination/(?P<id>\d+)$', views.destination, name='destination'),
]
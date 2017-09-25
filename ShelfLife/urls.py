from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<usr>[0-9]+)$', views.detail, name='details'),
    url(r'^add$', views.add, name='add'),
    url(r'^save$', views.save, name='save'),
    url(r'^(?P<usr>[0-9]+)/makeConnections$', views.makeConnections, name='makeConnections'),
    url(r'^(?P<usr>[0-9]+)/delete$', views.delete, name='delete'),
    url(r'^(?P<thing>[0-9]+)/deletething$', views.tdelete, name='thingdel'),
]
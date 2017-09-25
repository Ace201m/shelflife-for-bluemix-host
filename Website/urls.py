from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.red),
    url(r'^admin/', admin.site.urls),
    url(r'^ShelfLife', include('ShelfLife.urls')),
]

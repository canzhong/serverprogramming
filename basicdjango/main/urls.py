from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from main import views

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  path("", views.home),
  path("brewers", views.brewers),
  path("bucks", views.bucks),
  path("marquette", views.marquette),
]

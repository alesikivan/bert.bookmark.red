from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('search', views.search),
    path('visualizer/find/clusters', views.find_clusters),
]

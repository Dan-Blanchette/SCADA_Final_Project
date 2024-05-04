from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="home-home"),
    path('live-graph/', views.live_graphs, name="home-graphs"),
]
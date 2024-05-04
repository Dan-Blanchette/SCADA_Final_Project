from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('mini-factory-control-mode/', views.control_mode, name="mini-factory-control-mode"),
    path('mini-factory-data-table/', views.data_table, name="mini-factory-data-table"),
]
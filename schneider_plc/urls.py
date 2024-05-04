from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('schneider-plc-control-mode/', views.control_mode, name="schneider-plc-control-mode"),
    path('schneider-plc-data-table/', views.data_table, name="schneider-plc-data-table"),
]
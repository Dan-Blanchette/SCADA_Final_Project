from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('spinter-control-mode/', views.control_mode, name="splinter-control-mode"),
    path('splinter-data-table/', views.data_table, name="splinter-data-table"),
    path('splinter-graph/', views.graph, name="splinter-graph"),
    path('receive-splinter-data/', views.receive_splinter_data, name="splinter-receive-data"),
]

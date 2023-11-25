from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('DojoIn',views.DojoIn),
    path('NinjaIn',views.NinjaIn),
]

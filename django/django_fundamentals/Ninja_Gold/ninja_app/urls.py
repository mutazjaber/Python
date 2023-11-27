from django.contrib import admin,include
from . import views

urlpatterns = [
    path('', views.index),
]

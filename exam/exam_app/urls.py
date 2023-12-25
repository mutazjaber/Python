from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('success', views.success),
    path('destroy', views.logout),
    path('login', views.login),
    path('add_pie', views.add_pie),
    path('dashboard',views.user_dashboard),
    path("delete/<int:id>",views.delete),
    path("pies/",views.show_pies),
    path('edit_pie/<int:id>',views.edit_form),
    path('edit_process/<int:id>', views.edit_process),
    path("pies/<int:id>",views.view_pie),
    path('vote/<id>',views.add_vote),   
    
    

]

from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('shows/new',views.render_template),
    path('shows/create',views.create),
    path('shows/<int:id>',views.showTV),
    path('shows/<int:id>/edit',views.editShow),
    path('shows/update',views.update),
    path('shows/<int:id>/delete',views.delete)
    
]

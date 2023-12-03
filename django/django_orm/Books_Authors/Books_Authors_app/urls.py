from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.add_book),
    path('add_this_book',views.add_this_book),
    path('view_book/<int:id>',views.view_books),
    path('add_author_to_this_book',views.add_auther_to_this_book),
    
    # ---------------------------------------------------------------------------
    path('add_authors',views.add_author),
    path('add_this_author',views.add_this_author),
    path('view_author/<int:id>',views.view_authors),
    path("add_book_to_this_author",views.add_book_to_this_author)
    
]
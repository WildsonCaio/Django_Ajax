from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('add_book/', views.add_book, name='add_book'), 
    path('delete_book/<int:id>/', views.delete_book, name='delete_book'), 
               ]
from . import views
from django.urls import path, include

app_name='second'
urlpatterns = [
    path('', views.index, name='index'),
    path('favourite', views.favourites, name='favourites'),
    path('favourite/<int:idn>', views.favourites_detail, name='favourites_detail'),
    path('todo', views.todo, name='todos'),
    path('todo/<int:idn>', views.todo_detail, name='todo_detail'),
]
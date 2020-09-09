from . import views
from django.urls import path, include

app_name='second'
urlpatterns = [
    path('', views.index, name='index'),
    path('favourite', views.favourites, name='favourites'),
    path('favourite/<int:idn>', views.favourites_detail, name='favourites_detail'),
    path('favourite/register', views.favourites_add, name='favourites_add'),
    path('todo', views.todo, name='todos'),
    path('todo/<int:idn>', views.todo_detail, name='todo_detail'),
    path('todo/register', views.todo_add, name='todo_add'),
]
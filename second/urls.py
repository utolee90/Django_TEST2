from . import views
from django.urls import path, include

app_name='second'
urlpatterns = [
    path('', views.index, name='index'),
    path('favourite', views.favourites, name='favourites'),
    path('favourite/<int:idn>', views.favourites_detail, name='favourites_detail'),
    path('favourite/register', views.favourites_add, name='favourites_add'),
    path('favourite/modify/<int:idn>', views.favourites_modify, name='favourites_modify'),
    path('favourite/delete', views.favourites_delete, name='favourites_delete'),
    path('favourite/quick', views.favourites_quick, name='favourites_quick'), # get 방식으로 삭제하는 옵션 추가
    path('todo', views.todo, name='todos'),
    path('todo/<int:ids>', views.todo_detail, name='todo_detail'),
    path('todo/register', views.todo_add, name='todo_add'),
    path('todo/modify/<int:ids>', views.todo_modify, name='todo_modify'),
    path('todo/delete', views.todo_delete, name='todo_delete'),
    path('todo/quick', views.todo_quick, name='todo_quick'),
    path('todo/shift', views.todo_shift, name='todo_shift'),
    path('signup', views.signup, name='signup'),
    path('login', views.signin, name='login'),
    path('logout', views.signout, name='logout'),
]
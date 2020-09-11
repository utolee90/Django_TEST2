from . import views
from django.urls import path, include

app_name='first'

urlpatterns = [
    path('', views.index, name='index'),
    path('students', views.students, name='students'),
    path('students/<int:id>', views.students_detail, name='students_detail'),
    path('students/add', views.students_add, name='students_add'),
    path('students/del', views.students_del, name='students_del'),
    path('students/modify/<int:id>', views.students_modify, name='students_modify'),
    path('scores', views.scores, name='scores'), 
    path('scores/add', views.scores_add, name='scores_add'),
    path('scores/del', views.scores_del, name='scores_del'),
    path('makecookie/<name>', views.make_cookie, name='make_cookie')
]
from . import views
from django.urls import path, include

app_name='first'

urlpatterns = [
    path('', views.index, name='index'),
    path('students', views.students, name='students'),
    path('students/<int:id>', views.students_detail, name='students_detail'),
    path('scores', views.scores, name='scores'), 
    path('scores/del', view.scores_del, name='scores_del')
]
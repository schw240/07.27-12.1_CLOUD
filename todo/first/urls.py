from . import views
from django.urls import path, include
app_name = 'first'
urlpatterns = [
    path('', views.index, name='index'),
    path('students', views.students, name='students'),
    path('students/add', views.students_add, name='students_add'),
    path('students/<int:id>', views.students_detail, name='students'),
    path('scores', views.scores, name='scores'),
    path('scores/add', views.scores_add, name='scores_add')
    #path(URL경로 TEXT, views (함수들), 이름!)
]   
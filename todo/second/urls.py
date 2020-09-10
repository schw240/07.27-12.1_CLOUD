from . import views
from django.urls import path, include

app_name = 'second'

urlpatterns = [
    path('', views.index, name='index'),
    path('favourite', views.favourite, name='favourite'),
    path('favourite/<seq>', views.favourite_detail, name='favourite_detail'),
    path('todo', views.todo, name='todo'),
    path('todo/<seq>', views.todo_detail, name='todo_detail'),
]
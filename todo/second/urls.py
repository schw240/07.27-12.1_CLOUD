from . import views
from django.urls import path, include

app_name = 'second'

urlpatterns = [
    path('', views.index, name='index'),
    path('favourite', views.favourite, name='favourite'),
    path('todo', views.todo, name='todo'),
]   

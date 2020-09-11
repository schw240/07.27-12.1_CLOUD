from . import views
from django.urls import path, include

app_name = 'second'

urlpatterns = [
    path('', views.index, name='index'),
    path('favourite', views.favourite, name='favourite'),
    path('favourite/register', views.favourite_register, name='favourite_register'),
    path('favourite/<seq>', views.favourite_detail, name='favourite_detail'),
    path('favourite/<seq>/modify', views.favourite_modify, name='favourite_modify'),
    path('todo', views.todo, name='todo'),
    path('todo/register', views.todo_register, name='todo_register'),
    path('todo/<seq>', views.todo_detail, name='todo_detail'),
    path('todo/<seq>/modify', views.todo_modify, name='todo_modify'),
    path('favourite/<seq>/delete', views.favourite_delete, name='favourite_delete'),
    path('todo/<seq>/delete', views.todo_delete, name='todo_delete'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout_view, name='logout'),
]
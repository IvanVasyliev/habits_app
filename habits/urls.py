from venv import create
from django.urls import path

from . import views

urlpatterns = [
    path('create_user', views.create_user, name='create_user'),
    path('create_habit', views.create_habit, name='create_habit'),
    path('register_user_for_habit', views.register_user_for_habit, name='register_user_for_habit'),
    path('new_habit_action', views.new_habit_action, name='new_habit_action'),

    path('get_user_info', views.get_user_info, name='get_user_info'),
    path('get_habit_rating', views.get_habit_rating, name='get_habit_rating')
]
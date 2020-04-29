from django.urls import path
from .views import TodoList, Update, create, delete



urlpatterns = [
    path('', TodoList, name='todo-list'),
    path('create/', create, name='create'),
    path('update/<id>', Update, name='update'),
    path('delete/<id>', delete, name='delete'),

]
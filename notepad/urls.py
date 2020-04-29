from django.urls import path
from .views import create_view, list_view, delete_view, update_view


urlpatterns = [
    path('create/', create_view, name='create'),
    path('list/', list_view, name='list'),
    path('delete/<id>/', delete_view, name='delete'),
    path('update/<id>/', update_view, name='update'),

]

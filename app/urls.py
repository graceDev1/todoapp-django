from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('add_todo/', views.todo_action),
    path('delete/<int:todo_id>/', views.delete)
]
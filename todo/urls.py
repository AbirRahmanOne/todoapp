from django.urls import path
from .import views

from  todo.views import TaskView

from . import views

urlpatterns = [
    path('',TaskView.as_view(), name='list'),
    #path('',views.index, name="list"),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete")
]

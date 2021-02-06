from django.urls import path, include
from api.views import *

urlpatterns = [
    path('', apiOverview, name = 'apiOverview'),
    path('task-list/', showAllTasks, name = 'showAllTasks'),
    path('task-list/<int:pk>', showTask, name = 'showTask'),
    path('task-create/', createTask, name = 'createTask'),
    path('task-update/<int:pk>', updateTask, name = 'updateTask'),
    path('task-delete/<int:pk>', deleteTask, name = 'deleteTask'),
]
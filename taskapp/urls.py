from django.urls import path
from . import views

urlpatterns = [
    path("", views.TasksView.as_view(), name="task_list"),
    path("<int:pk>/", views.TaskDetailView.as_view(), name="task_detail")
]

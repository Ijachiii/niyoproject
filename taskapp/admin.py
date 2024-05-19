from django.contrib import admin
from .models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    """
    Custom admin model for the Task model.

    Attributes:
        model (Task): The model being registered.
        list_display (tuple): Fields to display in the admin list view.
    """
    model = Task
    list_display = ("user", "title", "completed", "date_created", "due_date")


admin.site.register(Task, TaskAdmin)

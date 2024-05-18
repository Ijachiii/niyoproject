from django.contrib import admin
from .models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = ("user", "title", "completed", "date_created", "due_date")


admin.site.register(Task, TaskAdmin)

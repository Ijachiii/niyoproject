from django.db import models
from accounts.models import CustomUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Task(models.Model):
    """
    Task model to represent tasks in the task management system.

    Attributes:
        title (CharField): The title of the task, with a maximum length of 200 characters.
        completed (BooleanField): A boolean field indicating whether the task is completed. Defaults to False.
        due_date (DateField): The due date for the task.
        date_created (DateTimeField): The date and time when the task was created. Automatically set to the current date and time when the task is created.
        user (ForeignKey): A foreign key relationship to the CustomUser model, representing the user who created the task. If the user is deleted, their tasks are also deleted.
    """
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    due_date = models.DateField()
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)
    user = models.ForeignKey(
        CustomUser, related_name="user_task", on_delete=models.CASCADE)

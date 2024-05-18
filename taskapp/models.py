from django.db import models
from accounts.models import CustomUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    due_date = models.DateField()
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)
    user = models.ForeignKey(
        CustomUser, related_name="user_task", on_delete=models.CASCADE)

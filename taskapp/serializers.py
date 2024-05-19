from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.

    This serializer translates Task model instances into JSON format and validates the data when creating or updating tasks.

    Attributes:
        Meta (class): Meta class to specify the model and fields to be included in the serialization.
    """
    class Meta:
        model = Task
        fields = ("title", "completed", "date_created", "due_date")

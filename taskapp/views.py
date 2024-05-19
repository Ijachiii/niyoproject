from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer

# Create your views here.


class TasksView(APIView):
    """
    View to handle creating and retrieving tasks.

    Attributes:
        permission_classes (list): List of permissions required to access the view.
        serializer_class (class): The serializer class used for validating and serializing data.
    """
    permission_classes = [IsAuthenticated,]
    serializer_class = TaskSerializer

    def get(self, request):
        """
        GET method to retrieve all tasks for the authenticated user.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: A JSON response containing the list of tasks and status code 200.
        """
        tasks = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(tasks, many=True)

        return Response({
            "data": serializer.data,
            "message": "Success",
            "error": False
        }, status=status.HTTP_200_OK)

    def post(self, request):
        """
        POST method to create a new task for the authenticated user.

        Args:
            request (Request): The HTTP request object containing task data.

        Returns:
            Response: A JSON response with the created task data and status code 200, or errors and status code 400.
        """
        serializer = TaskSerializer(data=request.data)
        print(request.user.id)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                "data": serializer.data,
                "message": "Task created successfully",
                "error": False,
            }, status=status.HTTP_200_OK)

        return Response({
            "data": None,
            "errorMessage": serializer.errors,
            "error": True,
        }, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    """
    View to handle retrieving, updating, and deleting a specific task.

    Attributes:
        permission_classes (list): List of permissions required to access the view.
        serializer_class (class): The serializer class used for validating and serializing data.
    """
    permission_classes = [IsAuthenticated,]
    serializer_class = TaskSerializer

    def get(self, request, pk=None):
        """
        GET method to retrieve a specific task by primary key.

        Args:
            request (Request): The HTTP request object.
            pk (int, optional): The primary key of the task.

        Returns:
            Response: A JSON response with the task data and status code 200, or errors and status code 400.
        """
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({
                "data": None,
                "errorMessage": [{
                    "code": "invalid_pk",
                    "message": "Task with this pk does not exist"
                }],
                "error": True
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = TaskSerializer(task)
        return Response({
            "data": serializer.data,
            "message": "Success",
            "error": False
        }, status=status.HTTP_200_OK)

    def patch(self, request, pk=None):
        """
        PATCH method to update a specific task by primary key.

        Args:
            request (Request): The HTTP request object containing task data.
            pk (int, optional): The primary key of the task.

        Returns:
            Response: A JSON response with the updated task data and status code 200, or errors and status code 400.
        """
        try:
            task = Task.object.get(pk=pk)
        except Task.DoesNotExist:
            return Response({
                "data": None,
                "errorMessage": [{
                    "code": "invalid_pk",
                    "message": "Task with this pk does not exist"
                }],
                "error": True
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = TaskSerializer(task, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "data": serializer.data,
                "message": "Taks updated successfully",
                "error": False
            }, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        """
        DELETE method to delete a specific task by primary key.

        Args:
            request (Request): The HTTP request object.
            pk (int, optional): The primary key of the task.

        Returns:
            Response: A JSON response indicating success and status code 200, or errors and status code 400.
        """
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({
                "data": None,
                "errorMessage": [{
                    "code": "invalid_pk",
                    "message": "FAQ with this pk does not exist"
                }],
                "error": True
            }, status=status.HTTP_400_BAD_REQUEST)

        task.delete()

        return Response({
            "data": None,
            "message": "FAQ deleted successfully",
            "error": False
        }, status=status.HTTP_200_OK)

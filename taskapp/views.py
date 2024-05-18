from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer

# Create your views here.


class TasksView(APIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = TaskSerializer

    def get(self, request):
        tasks = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(tasks, many=True)

        return Response({
            "data": serializer.data,
            "message": "Success",
            "error": False
        }, status=status.HTTP_200_OK)

    def post(self, request):
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
    permission_classes = [IsAuthenticated,]
    serializer_class = TaskSerializer

    def get(self, request, pk=None):
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

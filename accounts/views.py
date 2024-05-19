from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, LoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import login
from .models import CustomUser
from rest_framework.permissions import AllowAny

# Create your views here.


class UserSignUpView(APIView):
    """
    API view to handle user sign up.

    Attributes:
        serializer_class (UserSerializer): Serializer class for user sign up.
    """
    serializer_class = UserSerializer

    def post(self, request):
        """
        Handle POST request to create a new user.

        Args:
            request (Request): The request object containing user data.

        Returns:
            Response: The response object with user data and status code.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    """
    API view to handle user login and JWT token generation.

    Attributes:
        serializer_class (LoginSerializer): Serializer class for user login.
    """
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        """
        Handle POST request to authenticate user and return JWT tokens.

        Args:
            request (Request): The request object containing login credentials.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: The response object with JWT tokens and user data, or error message and status code.
        """
        serializer = LoginSerializer(data=request.data)
        if "email" in request.data:
            email = serializer.initial_data["email"]

            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                return Response({
                    "data": None,
                    "errorMessage": [{
                        "code": "invalid_credentials",
                        "message": "No active account found with the given credentials"
                    }],
                    "error": True,
                }, status=status.HTTP_401_UNAUTHORIZED)

        if serializer.is_valid():
            user = serializer.user
            login(request, user)

            return Response({
                "data": {
                    "access_token": serializer.validated_data["access"],
                    "refresh_token": serializer.validated_data["refresh"],
                    "id": user.id,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                },
                "message": "login successful",
                "error": False
            }, status=status.HTTP_200_OK)

        return Response({
            "data": None,
            "errorMessage": serializer.errors,
            "error": True,
        }, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenRefreshView(TokenRefreshView):
    """
    Custom token refresh view for refreshing JWT tokens.

    This view extends the TokenRefreshView provided by the rest_framework_simplejwt library.
    It overrides the default behavior to return a custom response format.

    Attributes:
        permission_classes (list): List of permission classes applied to the view.
        serializer_class: Serializer class used for token refreshing (set to None by default).
    """
    permission_classes = [AllowAny,]
    serializer_class = None

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        return Response({
            "data": response.data,
            "message": "Success",
            "error": False
        }, status=status.HTTP_200_OK)

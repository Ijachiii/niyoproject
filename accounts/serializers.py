from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and retrieving user instances.

    Attributes:
        password (CharField): A write-only field for the user's password.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name", "password")

    def create(self, validated_data):
        """
        Create and return a new user instance, given the validated data.

        Args:
            validated_data (dict): The validated data from the serializer.

        Returns:
            CustomUser: The created user instance.
        """
        user = CustomUser(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class LoginSerializer(TokenObtainPairSerializer):
    """
    Serializer for user login, generating JWT tokens.

    This serializer extends TokenObtainPairSerializer to include additional
    user data in the token response if necessary.
    """

    def validate(self, attrs):
        """
        Validate the login credentials and return JWT tokens.

        Args:
            attrs (dict): The input data containing login credentials.

        Returns:
            dict: A dictionary containing the JWT tokens and possibly additional data.
        """
        data = super().validate(attrs)
        return data

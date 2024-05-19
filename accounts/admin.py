from django.contrib import admin
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    """
    CustomUserAdmin defines the admin interface for the CustomUser model.

    Attributes:
        model (CustomUser): The model being registered with the admin interface.
        list_display (tuple): The fields to be displayed in the list view of the admin panel.
    """
    model = CustomUser
    list_display = ("email", "first_name", "last_name", "date_joined")


admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .forms import CustomUserChangeForm,CustomUserCreationForm


class CustomUseradmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = get_user_model()
    
    list_display = ("username", "email", "first_name", "last_name", "age", "is_staff")

    fieldsets = UserAdmin.fieldsets + (
        ("Additional information", {"classes": ("wide",), "fields": ("age",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "age",
                    "password1",
                    "password2",
                ),
            },
        ),
    )




from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from . import models


class UserAdministrator(UserAdmin):
    list_display = (
        "email",
        "firstname",
        "lastname",
        "last_login",
        "date_joined",
        "is_active",
    )
    list_display_links = ("email", "firstname", "lastname")
    readonly_fields = ("last_login", "date_joined")
    ordering = ("-date_joined",)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("User details"),
            {"fields": ("firstname", "lastname", "mobile", "gender", "birthday")},
        ),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser")}),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        None,
        {
            "classes": ("wide",),
            "fields": (
                "email",
                "password1",
                "password2",
                "firstname",
                "lastname",
                "mobile",
                "gender",
                "birthday",
                "is_active",
                "is_staff",
                "is_superuser",
            ),
        },
    )

admin.site.register(models.User, UserAdministrator)
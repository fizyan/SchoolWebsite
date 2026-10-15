from django.contrib import admin
from .models import AdmissionEnquiry


@admin.register(AdmissionEnquiry)
class AdmissionEnquiryAdmin(admin.ModelAdmin):

    list_display = (
        "student_name",
        "parent_name",
        "phone",
        "class_interested",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "class_interested",
        "created_at",
    )

    search_fields = (
        "student_name",
        "parent_name",
        "phone",
        "email",
    )

    list_editable = (
        "status",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "-created_at",
    )

    fieldsets = (
        (
            "Student Information",
            {
                "fields": (
                    "student_name",
                    "class_interested",
                )
            },
        ),
        (
            "Parent / Guardian Information",
            {
                "fields": (
                    "parent_name",
                    "phone",
                    "email",
                )
            },
        ),
        (
            "Enquiry Details",
            {
                "fields": (
                    "message",
                    "status",
                )
            },
        ),
        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )
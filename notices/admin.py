from django.contrib import admin

from .models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "published_at",
        "is_important",
        "is_active",
    )

    list_filter = (
        "is_important",
        "is_active",
        "published_at",
    )

    search_fields = (
        "title",
        "description",
    )

    list_editable = (
        "is_important",
        "is_active",
    )

    readonly_fields = (
        "published_at",
    )

    ordering = (
        "-published_at",
    )
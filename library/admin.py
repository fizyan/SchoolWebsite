# ============================================================
# 5. library/admin.py
# ============================================================

from django.contrib import admin
from .models import LibraryCategory, BookPDF


@admin.register(LibraryCategory)
class LibraryCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "book_count",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = ("name",)

    def book_count(self, obj):
        return obj.books.count()

    book_count.short_description = "Resources"


@admin.register(BookPDF)
class BookPDFAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "author",
        "is_featured",
        "is_active",
        "uploaded_at",
    )

    list_filter = (
        "category",
        "is_featured",
        "is_active",
        "uploaded_at",
    )

    search_fields = (
        "title",
        "author",
        "description",
        "category__name",
    )

    list_editable = (
        "is_featured",
        "is_active",
    )

    readonly_fields = (
        "uploaded_at",
    )

    autocomplete_fields = (
        "category",
    )

    ordering = (
        "-uploaded_at",
    )

    fieldsets = (
        (
            "Book Information",
            {
                "fields": (
                    "title",
                    "category",
                    "author",
                    "description",
                )
            }
        ),
        (
            "Files",
            {
                "fields": (
                    "cover_image",
                    "pdf_file",
                )
            }
        ),
        (
            "Publishing",
            {
                "fields": (
                    "is_featured",
                    "is_active",
                    "uploaded_at",
                )
            }
        ),
    )
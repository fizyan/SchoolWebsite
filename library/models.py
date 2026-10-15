# library/models.py

from django.db import models


class LibraryCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Library Category"
        verbose_name_plural = "Library Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class BookPDF(models.Model):
    category = models.ForeignKey(
        LibraryCategory,
        on_delete=models.CASCADE,
        related_name="books"
    )

    title = models.CharField(max_length=200)

    author = models.CharField(
        max_length=150,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    cover_image = models.ImageField(
        upload_to="library/covers/",
        blank=True,
        null=True
    )

    pdf_file = models.FileField(
        upload_to="library/pdfs/"
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return self.title
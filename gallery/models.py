from django.db import models


class GalleryCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    title = models.CharField(max_length=255)

    category = models.ForeignKey(
        GalleryCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="images",
    )

    image = models.ImageField(
        upload_to="gallery/",
    )

    description = models.TextField(
        blank=True,
    )

    is_published = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
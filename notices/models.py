from django.db import models


class Notice(models.Model):
    title = models.CharField(max_length=200)

    description = models.TextField()

    attachment = models.FileField(
        upload_to="notices/",
        blank=True,
        null=True
    )

    published_at = models.DateTimeField(
        auto_now_add=True
    )

    is_important = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title
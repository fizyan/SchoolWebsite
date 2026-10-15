from django.db import models


class AdmissionEnquiry(models.Model):

    STATUS_CHOICES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("in_progress", "In Progress"),
        ("admitted", "Admitted"),
        ("closed", "Closed"),
    ]

    parent_name = models.CharField(max_length=150)
    student_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    class_interested = models.CharField(
        max_length=100,
        default="Not Specified",
    )
    message = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Admission Enquiry"
        verbose_name_plural = "Admission Enquiries"

    def __str__(self):
        return f"{self.student_name} - {self.parent_name}"
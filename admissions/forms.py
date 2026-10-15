from django import forms
from .models import AdmissionEnquiry


class AdmissionEnquiryForm(forms.ModelForm):

    class Meta:
        model = AdmissionEnquiry

        fields = [
            "parent_name",
            "student_name",
            "phone",
            "email",
            "class_interested",
            "message",
        ]

        widgets = {
            "parent_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Parent / Guardian Name",
                }
            ),
            "student_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Student Name",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Phone Number",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email Address",
                }
            ),
            "class_interested": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Class Interested In",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Write your enquiry...",
                    "rows": 5,
                }
            ),
        }
        
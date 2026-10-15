from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import AdmissionEnquiryForm


def admission_home(request):

    if request.method == "POST":
        form = AdmissionEnquiryForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Your admission enquiry has been submitted successfully. "
                "Our school team will contact you soon.",
            )

            return redirect("admissions:home")

    else:
        form = AdmissionEnquiryForm()

    return render(
        request,
        "admissions/home.html",
        {
            "form": form,
        },
    )
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactMessageForm


def home(request):
    return render(request, "school/home.html")


def about(request):
    return render(request, "school/about.html")


def academics(request):
    return render(request, "school/academics.html")


def faculty(request):
    return render(request, "school/faculty.html")


def facilities(request):
    return render(request, "school/facilities.html")


def contact(request):

    if request.method == "POST":
        form = ContactMessageForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("school:contact")

    else:
        form = ContactMessageForm()

    return render(
        request,
        "school/contact.html",
        {
            "form": form,
        },
    )


def demo(request):
    return render(request, "school/demo.html")


def demo_navy(request):
    return render(request, "school/demo_navy.html")


def demo_charcoal(request):
    return render(request, "school/demo_charcoal.html")
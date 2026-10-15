from django.shortcuts import render

from .models import Notice


def notice_list(request):
    notices = Notice.objects.filter(
        is_active=True
    )

    context = {
        "notices": notices,
    }

    return render(
        request,
        "notices/list.html",
        context
    )
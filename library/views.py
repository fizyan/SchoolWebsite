# ============================================================
# 1. library/views.py
# ============================================================

from django.shortcuts import render
from django.db.models import Q

from .models import BookPDF, LibraryCategory


def library_home(request):
    query = request.GET.get("q", "").strip()
    category_id = request.GET.get("category", "").strip()

    books = BookPDF.objects.filter(
        is_active=True
    ).select_related("category")

    if query:
        books = books.filter(
            Q(title__icontains=query)
            | Q(author__icontains=query)
            | Q(description__icontains=query)
            | Q(category__name__icontains=query)
        )

    if category_id:
        books = books.filter(category_id=category_id)

    categories = LibraryCategory.objects.all()

    featured_books = BookPDF.objects.filter(
        is_active=True,
        is_featured=True
    ).select_related("category")[:6]

    context = {
        "books": books,
        "categories": categories,
        "featured_books": featured_books,
        "query": query,
        "selected_category": category_id,
    }

    return render(request, "library/home.html", context)
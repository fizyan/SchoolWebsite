from django.shortcuts import render
from .models import GalleryCategory, GalleryImage


def gallery_home(request):
    categories = GalleryCategory.objects.all()
    images = GalleryImage.objects.filter(
        is_published=True
    ).select_related("category")

    selected_category = request.GET.get("category")

    if selected_category:
        images = images.filter(category_id=selected_category)

    context = {
        "categories": categories,
        "images": images,
        "selected_category": selected_category,
    }

    return render(request, "gallery/home.html", context)
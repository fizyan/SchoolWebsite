
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),

    # Main website
    path("", include("school.urls")),

    # Website modules
    path("library/", include("library.urls")),
    path("notices/", include("notices.urls")),
    path("events/", include("events.urls")),
    path("gallery/", include("gallery.urls")),
    path("admissions/", include("admissions.urls")),
]

# Serve uploaded media files during development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )


from admissions.models import AdmissionEnquiry
from events.models import Event
from gallery.models import GalleryImage
from library.models import BookPDF
from notices.models import Notice
from .models import ContactMessage


def admin_dashboard_stats(request):
    if not request.path.startswith("/admin/"):
        return {}

    return {
        "dashboard_admissions": AdmissionEnquiry.objects.count(),
        "dashboard_new_admissions": AdmissionEnquiry.objects.filter(
            status="new"
        ).count(),
        "dashboard_messages": ContactMessage.objects.count(),
        "dashboard_new_messages": ContactMessage.objects.filter(
            status="new"
        ).count(),
        "dashboard_notices": Notice.objects.filter(is_active=True).count(),
        "dashboard_events": Event.objects.filter(is_published=True).count(),
        "dashboard_books": BookPDF.objects.filter(is_active=True).count(),
        "dashboard_gallery": GalleryImage.objects.filter(
            is_published=True
        ).count(),
    }

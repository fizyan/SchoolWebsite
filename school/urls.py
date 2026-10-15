from django.urls import path

from . import views

app_name = "school"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("academics/", views.academics, name="academics"),
    path("faculty/", views.faculty, name="faculty"),
    path("facilities/", views.facilities, name="facilities"),
    path("contact/", views.contact, name="contact"),
    path("demo/", views.demo, name="demo"),
    path("demo-navy/", views.demo_navy, name="demo_navy"),
    path("demo-charcoal/", views.demo_charcoal, name="demo_charcoal"),
]
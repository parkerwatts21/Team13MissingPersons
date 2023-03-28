from django.urls import path
from .views import indexPageView, aboutPageView, analysisPageView, contactPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("about/", aboutPageView, name="about"),
    path("analysis/", analysisPageView, name="analysis"),
    path("contact/", contactPageView, name="contact"),
]

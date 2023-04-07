from django.urls import path
from .views import indexPageView, aboutPageView, dataPageView, displayPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("about/", aboutPageView, name="about"),
    path("data/", dataPageView, name="data"),
    path("display/", displayPageView, name="display"),
]

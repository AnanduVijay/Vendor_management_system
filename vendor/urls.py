from django.urls import path, include


urlpatterns = [
    path("api/", include("vendor.api.urls")),
]

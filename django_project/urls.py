from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("blogs.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")),
    path(
        "api/v1/dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")
    ),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/redoc", SpectacularRedocView.as_view(), name="schema-redoc"),
    path("api/schema/swagger", SpectacularSwaggerView.as_view(), name="schema-swagger"),
]

from django.urls import include, path

urlpatterns = [
    path("kitchen/", include("apps.kitchen.urls")),
    path("users/", include("apps.users.urls")),
]

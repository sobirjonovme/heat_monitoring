from django.urls import include, path

urlpatterns = [
    path("chicken-farm/", include("apps.chicken_farm.urls")),
    path("kitchen/", include("apps.kitchen.urls")),
    path("users/", include("apps.users.urls")),
]

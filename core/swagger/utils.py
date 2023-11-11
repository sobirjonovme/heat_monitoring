from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from core.swagger.generator import BothHttpAndHttpsSchemaGenerator

main_schema_view = get_schema_view(
    openapi.Info(
        title="HEAT Monitoring API",
        default_version="v1",
        description="HEAT Monitoring API",
        contact=openapi.Contact(email="muhandis.asadbek@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    generator_class=BothHttpAndHttpsSchemaGenerator,
)


chicken_farm_schema_view = get_schema_view(
    openapi.Info(
        title="HEAT Monitoring API",
        default_version="v1",
        description="HEAT Monitoring API",
        contact=openapi.Contact(email="muhandis.asadbek@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    generator_class=BothHttpAndHttpsSchemaGenerator,
    patterns=[
        # path("api/v1/common/", include("apps.common.urls")),
        # path("api/v1/users/", include("apps.users.urls")),
        path("api/v1/chicken-farm/", include("apps.chicken_farm.urls")),
    ],
)

kitchen_schema_view = get_schema_view(
    openapi.Info(
        title="HEAT Monitoring API",
        default_version="v1",
        description="HEAT Monitoring API",
        contact=openapi.Contact(email="muhandis.asadbek@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    generator_class=BothHttpAndHttpsSchemaGenerator,
    patterns=[
        path("api/v1/kitchen/", include("apps.kitchen.urls")),
    ],
)

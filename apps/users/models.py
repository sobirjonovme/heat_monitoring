from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class UserRoles(models.TextChoices):
    ADMIN = "admin", _("Admin")
    # for KITCHEN
    COOK = "cook", _("Cook")
    PROVIDER = "provider", _("Provider")
    # for CHICKEN FARM
    FARM_COUNTER = "farm_counter", _("Farm Counter")


class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=UserRoles.choices,
        default=UserRoles.ADMIN,
    )

    def is_admin(self):
        return self.role == UserRoles.ADMIN

    def is_cook(self):
        return self.role == UserRoles.COOK

    def is_provider(self):
        return self.role == UserRoles.PROVIDER

    def is_farm_counter(self):
        return self.role == UserRoles.FARM_COUNTER

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class UserRoles(models.TextChoices):
    ADMIN = "admin", _("Admin")
    COOK = "cook", _("Cook")
    PROVIDER = "provider", _("Provider")


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

from django.db import models
from django.utils.translation import gettext_lazy as _


class RoomTypeChoices(models.TextChoices):
    """Room Type Choices"""

    FOCUS = "focus", _("Focus")
    TEAM = "team", _("Team")
    CONFERENCE = "conference", _("Conference")

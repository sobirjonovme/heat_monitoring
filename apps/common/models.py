from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(verbose_name=_("created at"), auto_now_add=True)  # auto_now_add: when created
    updated_at = models.DateTimeField(verbose_name=_("updated at"), auto_now=True)  # auto_now: when updated

    class Meta:
        abstract = True  # abstract: not to migrate to DB

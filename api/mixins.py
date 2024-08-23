from django.db import models
from django.utils.translation import gettext_lazy as _


class CreatedUpdatedMixin(models.Model):
    created_at = models.DateTimeField(
        verbose_name=_("Date of creation"),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Date of last update"),
        auto_now=True
    )

    class Meta:
        abstract = True


class AdminPageLimit:
    list_per_page = 25

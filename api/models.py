from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from . import mixins

User = settings.AUTH_USER_MODEL


class Stock(models.Model):
    title = models.CharField(
        verbose_name=_('Name'),
        max_length=100,
        unique=True
    )
    address = models.CharField(
        verbose_name=_('Address'),
        max_length=150
    )

    class Meta:
        indexes = (
            models.Index(fields=('address',)),
        )
        verbose_name = _('Warehouse')
        verbose_name_plural = _('Warehouses')

    def __str__(self) -> str:
        return f'[{self.title[:15]}] {self.address[:50]}'


class Category(models.Model):
    title = models.CharField(
        verbose_name=_('Name'),
        max_length=100,
        unique=True
    )

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self) -> str:
        return f'{self.title}'


class Equipment(mixins.CreatedUpdatedMixin, models.Model):
    title = models.CharField(
        verbose_name=_('Name'),
        max_length=100,
        unique=True
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name=_('Ammount'),
        default=1
    )
    stock = models.ForeignKey(
        verbose_name=_('Warehouse'),
        to=Stock,
        on_delete=models.CASCADE,
        related_name='equipment'
    )
    category = models.ForeignKey(
        verbose_name=_('Catefory'),
        to=Category,
        on_delete=models.CASCADE,
        related_name='equipment'
    )
    user = models.ForeignKey(
        verbose_name=_('Owner'),
        to=User,
        on_delete=models.CASCADE,
        related_name='equipment'
    )

    class Meta:
        verbose_name = _('Equipment')
        verbose_name_plural = _('Equipment')

    def __str__(self) -> str:
        return f'[{self.title[:15]}] {self.quantity}'

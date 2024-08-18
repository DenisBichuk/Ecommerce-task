from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from . import mixins

User = settings.AUTH_USER_MODEL


class Stock(models.Model):
    title = models.CharField(
        verbose_name=_('Название'),
        max_length=100,
        unique=True
    )
    address = models.CharField(
        verbose_name=_('Адрес'),
        max_length=150
    )

    class Meta:
        indexes = (
            models.Index(fields=('address',)),
        )
        verbose_name = _('Склад')
        verbose_name_plural = _('Склады')

    def __str__(self) -> str:
        return f'[{self.title[:15]}] {self.address[:50]}'


class Category(models.Model):
    title = models.CharField(
        verbose_name=_('Название'),
        max_length=100,
        unique=True
    )

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    def __str__(self) -> str:
        return f'{self.title}'


class Equipment(mixins.CreatedUpdatedMixin, models.Model):
    title = models.CharField(
        verbose_name=_('Название'),
        max_length=100,
        unique=True
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name=_('Количество'),
        default=1
    )
    stock = models.ForeignKey(
        verbose_name=_('Склад'),
        to=Stock,
        on_delete=models.CASCADE,
        related_name='equipments'
    )
    category = models.ForeignKey(
        verbose_name=_('Категория'),
        to=Category,
        on_delete=models.CASCADE,
        related_name='equipments'
    )
    user = models.ForeignKey(
        verbose_name=_('Владелец'),
        to=User,
        on_delete=models.CASCADE,
        related_name='equipments'
    )

    class Meta:
        verbose_name = _('Оборудование')
        verbose_name_plural = _('Оборудования')

    def __str__(self) -> str:
        return f'[{self.title[:15]}] {self.quantity}'

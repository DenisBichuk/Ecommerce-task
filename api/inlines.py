from django.contrib import admin

from . import models


class EquipmentInline(admin.StackedInline):
    model = models.Equipment
    extra = 0

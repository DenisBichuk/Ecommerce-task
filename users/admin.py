from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.conf import settings
from django.contrib.admin import register
from django.contrib.auth import get_user_model

User = get_user_model()


@register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'is_staff',
                    'password1',
                    'password2',
                ),
            },
        ),
    )
    fieldsets = (
        (
            None,
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'is_active',
                    'is_superuser',
                    'password'
                ),
            },
        ),
    )
    list_display = (
        'id',
        'email',
        'first_name',
        'last_name',
        'date_joined',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    ordering = ('-id',)
    readonly_fields = ['date_joined', 'is_superuser']
    search_fields = ('email',)

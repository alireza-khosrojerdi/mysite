from django.contrib import admin
from accounts.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_joined'
    empty_value_display = 'empty'
    list_display = ('username', 'email', 'is_staff',
                    'is_superuser', 'date_joined')
    list_filter = ('is_active', 'is_superuser')
    search_fields = ['username', 'email']


admin.site.register(CustomUser, CustomUserAdmin)

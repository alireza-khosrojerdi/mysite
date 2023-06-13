from django.contrib import admin
from accounts.models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_joined'
    empty_value_display = 'empty'
    list_display = ('username','first_name','last_name','is_active','is_staff','is_superuser','last_login')
    list_filter = ('username', 'is_superuser')
    ordering = ['date_joined']
    search_fields = ['username', 'email']

admin.site.register(CustomUser, CustomUserAdmin)
    

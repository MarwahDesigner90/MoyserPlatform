from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Companion, DisabilityUser

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Roles and Permissions', {'fields': ('role', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)

@admin.register(Companion)
class CompanionAdmin(admin.ModelAdmin):
    list_display = ('companion', 'city', 'availability', 'hour_rent')
    list_filter = ('city', 'availability')

@admin.register(DisabilityUser)
class DisabilityUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'disability_type', 'age', 'gender')
    list_filter = ('disability_type', 'gender')


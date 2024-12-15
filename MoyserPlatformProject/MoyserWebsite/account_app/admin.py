from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Roles and Permissions', {'fields': ('role', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role', 'password1', 'password2', 'is_staff'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)

@admin.register(Companion)
class CompanionAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'availability', 'hour_rent')
    list_filter = ('city', 'availability')

@admin.register(DisabilityUser)
class DisabilityUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'disability_type', 'age', 'gender')
    list_filter = ('disability_type', 'gender')


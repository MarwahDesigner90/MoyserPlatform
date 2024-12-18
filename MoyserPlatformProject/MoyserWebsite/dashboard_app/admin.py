from django.contrib import admin
from django.utils.html import format_html
from account_app.models import Companion , DisabilityUser

# Register your models here.
class CompanionAdmin(admin.ModelAdmin):
    list_display = (
        'display_image',
        'companion_name',
        'username',
        'hour_rent',
        'phone_number',
        'view_certification',
        'skills_list',
        'email',
    )
    
    def display_image(self, obj):
        return format_html(
            '<img src="{}" style="width: 50px; height: auto;" />',
            obj.image.url if obj.image else 'images/default.jpeg'
        )
    display_image.short_description = 'Image'

    def companion_name(self, obj):
        return f"{obj.companion.first_name} {obj.companion.last_name}"
    companion_name.short_description = 'Companion Name'

    def username(self, obj):
        return obj.companion.username
    username.short_description = 'Username'

    def email(self, obj):
        return obj.companion.email
    email.short_description = 'Email'

    def hour_rent(self, obj):
        return f"${obj.hour_rent:.2f}"
    hour_rent.short_description = 'Rent per Hour'

    def phone_number(self, obj):
        return obj.phone_number
    phone_number.short_description = 'Phone Number'

    def view_certification(self, obj):
        if obj.certification:
            return format_html('<a href="{}" target="_blank">View Certificate</a>', obj.certification.url)
        return 'No Certificate'
    view_certification.short_description = 'Certificate'

    def skills_list(self, obj):
        return ", ".join([skill.name for skill in obj.skills.all()])
    skills_list.short_description = 'Skills'

# Register the Companion model with the custom admin class
admin.site.register(Companion, CompanionAdmin)


class DisabilityUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'get_disability_type', 'get_gender', 'age', 'address')
    search_fields = ('user__username', 'phone_number', 'address')
    list_filter = ('disability_type', 'gender')

    def get_disability_type(self, obj):
        return obj.get_disability_type_display()
    get_disability_type.short_description = 'Disability Type'

    def get_gender(self, obj):
        return obj.get_gender_display()
    get_gender.short_description = 'Gender'

# admin.site.register(DisabilityUser, DisabilityUserAdmin)
admin.site.register(DisabilityUser, DisabilityUserAdmin)



from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Patron, CheckIn

@admin.register(Patron)
class PatronAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Information', {
            'fields': ('picture', 'first_name', 'last_name', 
                        'birth_date', 'gender', 'phone', 'signature')
        }),
        ('Special Status', {
            'fields': ('veteran', 'violence', 'offender')
        }),
        ('History', {
            'fields': ('time_homeless', 'city', 'reason', 'other')
        })
    )

    readonly_fields = ["picture", "signature"]

    def picture(self, obj):
        return mark_safe('<img src="{url}" width="150" height="240" />'.format(
            url = obj.headshot.url,
        )
    )

    def signature(self, obj):
        return mark_safe('<img src="{url}" width="150" height="25" />'.format(
            url = obj.signature.url,
        )
    )
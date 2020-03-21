from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.timesince import timesince

from .models import Patron, CheckIn

@admin.register(Patron)
class PatronAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Information', {
            'fields': ('headshot_img', 'first_name', 'last_name', 
                        'birth_date', 'gender', 'phone', 'signature_img')
        }),
        ('Special Status', {
            'fields': ('veteran', 'violence', 'offender')
        }),
        ('History', {
            'fields': ('duration_homeless', 'city', 'reason', 'other')
        })
    )

    readonly_fields = ["headshot_img", "signature_img", 'duration_homeless']

    def headshot_img(self, obj):
        return mark_safe('<img src="{url}" width="150" height="240" />'.format(
            url = obj.headshot.url,
        )
    )
    headshot_img.short_description = 'Picture'

    def signature_img(self, obj):
        return mark_safe('<img src="{url}" width="240" height="40" />'.format(
            url = obj.signature.url,
        )
    )
    signature_img.short_description = 'Signature'

    def duration_homeless(self, obj):
        return timesince(obj.date_homeless)
    duration_homeless.short_description = 'Duration Homeless'

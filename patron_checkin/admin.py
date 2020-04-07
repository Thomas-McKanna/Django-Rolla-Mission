from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.timesince import timesince

from .models import Patron, CheckIn


class CheckInAdmin(admin.TabularInline):
    model = CheckIn
    readonly_fields = ['date']
    ordering = ["-date"]
    extra = 0


@admin.register(Patron)
class PatronAdmin(admin.ModelAdmin):
    list_display = ('name', 'veteran', 'violence', 'offender')
    list_filter = ('veteran', 'violence', 'offender',
                   'gender', 'date_homeless')
    search_fields = ('name',)

    inlines = [CheckInAdmin, ]

    fieldsets = (
        ('Personal Information', {
            'fields': ('headshot_img', 'name', 'birth_date', 'gender',
                       'phone', 'duration_homeless', 'signature_img', 
                       'date_profile_creation')
        }),
        ('Special Status', {
            'classes': ('collapse',),
            'fields': ('veteran', 'violence', 'offender')
        }),
        ('History', {
            'classes': ('collapse',),
            'fields': ('date_homeless', 'city', 'reason')
        }),
    )

    readonly_fields = ["headshot_img", "signature_img", 'duration_homeless', 'date_profile_creation']

    def headshot_img(self, obj):
        return mark_safe('<img src="{url}" width="196" />'.format(
            url=obj.headshot.url,)
        )
    headshot_img.short_description = 'Picture'

    def signature_img(self, obj):
        return mark_safe('<img src="{url}" width="240" height="40" />'.format(
            url=obj.signature.url,)
        )
    signature_img.short_description = 'Signature'

    def duration_homeless(self, obj):
        return timesince(obj.date_homeless)
    duration_homeless.short_description = 'Duration Homeless'

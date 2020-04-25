from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.timesince import timesince
from django import forms

from .models import Patron, CheckIn


class CheckInAdmin(admin.TabularInline):
    model = CheckIn
    readonly_fields = ['date']
    ordering = ["-date"]
    extra = 0


class MyModelForm(forms.ModelForm):
    GENDER_CHOICES = [
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other'),
            ('Prefer not to answer', 'Prefer not to answer'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    notes = forms.CharField(widget=forms.Textarea, required=False)


@admin.register(Patron)
class PatronAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_checkin', 'veteran', 'violence', 'offender')
    list_filter = ('last_checkin', 'veteran', 'violence', 'offender',
                   'gender')
    search_fields = ('name',)

    inlines = [CheckInAdmin, ]
    
    def get_fieldsets(self, request, obj=None):
        if obj:
            return (
                ('Personal Information', {
                    'fields': ('headshot_img', 'name', 'birth_date', 'gender',
                    'phone', 'duration_homeless', 'notes')
                }),
                ('Special Status', {
                    'classes': ('collapse',),
                    'fields': ('veteran', 'violence', 'offender')
                }),
                ('History', {
                    'classes': ('collapse',),
                    'fields': ('date_homeless', 'city', 'reason')
                }),
                ('Signature', {
                    'classes': ('collapse',),
                    'fields': ('signature_img', 'date_profile_creation')
                }),
            )
        else:
            return (
                ('Personal Information', {
                    'fields': ('name', 'birth_date', 'gender', 'phone', 'notes')
                }),
                ('Special Status', {
                    'fields': ('veteran', 'violence', 'offender')
                }),
                ('History', {
                    'fields': ('date_homeless', 'city', 'reason')
                }),
            )

    readonly_fields = ["headshot_img", "signature_img", 'duration_homeless', 'date_profile_creation']
    
    form = MyModelForm


    def headshot_img(self, obj):
        return mark_safe('<img src="{url}" width="196" />'.format(
            url=obj.headshot.url,)
        )
    headshot_img.short_description = 'Picture'

    def signature_img(self, obj):
        return mark_safe('<img src="{url}"  height="60" />'.format(
            url=obj.signature.url,)
        )
    signature_img.short_description = 'Signature'

    def duration_homeless(self, obj):
        return timesince(obj.date_homeless)
    duration_homeless.short_description = 'Duration Homeless'

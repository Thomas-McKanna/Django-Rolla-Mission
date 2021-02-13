from django.contrib import admin

from patron_checkin.models import CheckIn

# Register your models here.
@admin.register(CheckIn)
class PatronAdmin(admin.ModelAdmin):
    list_display = ('patron_id', 'date')
    date_hierarchy = 'date'

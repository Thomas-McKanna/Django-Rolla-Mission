from django.db import models
from django.utils import timezone
from django.contrib.admin.filters import DateFieldListFilter
from django.utils.translation import gettext_lazy as _
import datetime


class CustomDateFieldListFilter(DateFieldListFilter):
    def __init__(self, *args, **kwargs):
        super(CustomDateFieldListFilter, self).__init__(*args, **kwargs)

        now = timezone.now()
        # When time zone support is enabled, convert "now" to the user's time
        # zone so Django's definition of "Today" matches what the user expects.
        if timezone.is_aware(now):
            now = timezone.localtime(now)

        if isinstance(args[0], models.DateTimeField):
            today = now.replace(hour=0, minute=0, second=0, microsecond=0)
        else:       # field is a models.DateField
            today = now.date()
        one_day_past = today + datetime.timedelta(days=1)
        two_days_past = one_day_past + datetime.timedelta(days=1)
        three_days_past = two_days_past + datetime.timedelta(days=1)
        four_days_past = three_days_past + datetime.timedelta(days=1)

        self.links = (
            (_('Today'), {
                self.lookup_kwarg_since: str(today),
                self.lookup_kwarg_until: str(one_day_past),
            }),
            (_('One day ago'), {
                self.lookup_kwarg_since: str(one_day_past),
                self.lookup_kwarg_until: str(two_days_past),
            }),
            (_('Two days ago'), {
                self.lookup_kwarg_since: str(two_days_past),
                self.lookup_kwarg_until: str(three_days_past),
            }),
            (_('Three days ago'), {
                self.lookup_kwarg_since: str(three_days_past),
                self.lookup_kwarg_until: str(four_days_past),
            }),
        )

from patron_checkin.models import Patron
from django.views import generic
from datetime import datetime, timedelta

class IndexView(generic.ListView):
    template_name = 'patron_checkin/index.html'
    context_object_name = 'patron_list'

    def get_queryset(self):
        time_threshold = datetime.now() - timedelta(hours=12)
        return Patron.objects.filter(checkin__date__gt=time_threshold)

from patron_checkin.models import Patron
from django.views import generic
from datetime import datetime, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'patron_checkin/index.html'
    context_object_name = 'patron_list'

    def get_queryset(self):
        time_threshold = datetime.now() - timedelta(hours=12)
        return Patron.objects.filter(checkin__date__gt=time_threshold).order_by('-name')


def html_to_pdf_view(request):
    patrons = Patron.objects.all()
    html_string = render_to_string(
        'patron_checkin/report.html', {'patrons': patrons})

    html = HTML(string=html_string)

    response = HttpResponse(html.write_pdf(), content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="patron_report.pdf"'
    return response

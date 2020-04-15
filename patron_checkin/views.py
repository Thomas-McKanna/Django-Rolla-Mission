from patron_checkin.models import Patron
from django.views import generic
from datetime import datetime, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.http import FileResponse
from reportlab.lib.units import inch
from io import BytesIO
import requests
from PIL import Image
from reportlab.lib.utils import ImageReader

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'patron_checkin/index.html'
    context_object_name = 'patron_list'

    def get_queryset(self):
        time_threshold = datetime.now() - timedelta(hours=12)
        return Patron.objects.filter(checkin__date__gt=time_threshold).order_by('-name')

def generate_pdf(request=None):
    patron = Patron.objects.filter(_id='05ff7491-6bfa-4813-8791-1d56fb2681f5')[0]
    name = str(patron.name)
    dob = str(patron.birth_date)
    gender = patron.gender
    phone_num = patron.phone
    pic_url = patron.headshot.url
    sig_url = patron.signature.url
    response_pic = requests.get(pic_url)
    picture = Image.open(BytesIO(response_pic.content))
    picture.save(BytesIO(), format=picture.format)
    picture = BytesIO().getvalue()
    response_sig = requests.get(sig_url)
    signature = Image.open(BytesIO(response_sig.content))
    signature.save(BytesIO(), format=signature.format)
    signature = BytesIO().getvalue()
    current_time = datetime.now()
    file_name = 'Report for ' + name + '_' + str(current_time)[:-7] + '.pdf'
    buffer = BytesIO()
    p = canvas.Canvas(filename=file_name, pagesize=letter)
    p.setFont('Times-Roman', 16)
    p.drawString(0, 3 * inch, 'Patron Data')
    p.translate(-3.5 * inch, 0)
    p.drawString(0, 0, 'Name: ' + name)
    p.drawString(0, -1.5 * inch, 'Date of Birth: ' + dob)
    p.drawString(0, -3 * inch, 'Gender: ' + gender)
    p.drawString(0, -4.5 * inch, 'Phone Number: ' + phone_num)
    p.drawString(0, -6 * inch, 'Picture: ')
    p.drawImage(picture, 3 * inch, -6 * inch)
    p.drawString(0, -7.5 * inch, "Signature: ")
    p.drawImage(signature, 3 * inch, -7.5 * inch)
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, filename=file_name)
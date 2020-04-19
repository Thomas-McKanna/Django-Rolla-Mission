from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('pdf', views.html_to_pdf_view, name='report')
]
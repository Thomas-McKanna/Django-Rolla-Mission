from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('', views.generate_pdf(), name='generate_pdf')
]
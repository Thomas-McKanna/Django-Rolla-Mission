from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('patrons/', views.PatronList.as_view()),
    path('patrons/headshot/<uuid:pk>', views.UpdateHeadshot.as_view()),
    path('patrons/signature/<uuid:pk>', views.UpdateSignature.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
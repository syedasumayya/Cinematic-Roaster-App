from django.urls import path
from . import views

urlpatterns = [
    path('roast/', views.analyze_and_roast, name='analyze-roast'),
]
from django.urls import path
from .import views as contact_views

urlpatterns = [
    # Paths del contact
    path('', contact_views.contact, name="contact"),
]
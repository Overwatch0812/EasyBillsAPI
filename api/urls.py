from django.urls import path
from .views import *

urlpatterns = [
    path('create/',CreateInvoice.as_view())
]

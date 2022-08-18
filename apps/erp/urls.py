from django.urls import path

from apps.erp.views import *


urlpatterns = [
    path('lista/', myFirstView),
]
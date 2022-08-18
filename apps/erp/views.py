from django.http import HttpResponse
from django.shortcuts import render

from apps.erp.models import *

# Create your views here.
def myFirstView(request):
    data = {
        'name': 'William',
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'erp/index.html', data)